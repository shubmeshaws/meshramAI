```bash
#!/bin/bash

# Check if SCRIPT_DIR is set
if [ -z "$SCRIPT_DIR" ]; then
  log_error "SCRIPT_DIR variable is not set" 1
fi

# Check if LOG_FILE is set
if [ -z "$LOG_FILE" ]; then
  log_error "LOG_FILE variable is not set" 1
fi

function log_error() {
  # Log error message and exit with code
  local message="$1"
  local exit_code="$2"
  echo "[ERROR] $message" | tee -a "$LOG_FILE"
  exit "$exit_code"
}

function log_info() {
  # Log info message
  echo "[INFO] $1" | tee -a "$LOG_FILE"
}

function check_directory() {
  # Check if directory exists and is writable
  local dir="$1"
  if [ ! -d "$dir" ]; then
    log_error "Directory does not exist: $dir" 1
  elif [ ! -w "$dir" ]; then
    log_error "Directory is not writable: $dir" 1
  fi
  return 0
}

# Check if SCRIPT_DIR and LOG_FILE directories exist and are writable
if ! check_directory "$SCRIPT_DIR"; then
  exit 1
fi
if ! check_directory "$(dirname "$LOG_FILE")"; then
  exit 1
fi

function show_ec2_help() {
  # Display available EC2 service commands
  echo "EC2 service commands:"
  echo "  meshram ec2 create                 - Launch an EC2 instance"
  echo "  meshram ec2 list                   - List EC2 instances"
  echo "  meshram ec2 terminate <instance-id> - Terminate an EC2 instance"
}

function ec2_handler() {
  # Input validation for ec2_handler function
  if [ $# -eq 0 ]; then
    show_ec2_help
    return
  fi

  local cmd="$1"
  shift
  case "$cmd" in
    help|"")
      show_ec2_help
      ;;
    create)
      ec2_create
      ;;
    list)
      ec2_list
      ;;
    terminate)
      # Check if instance-id is provided
      if [ $# -ne 1 ]; then
        log_error "Usage: meshram ec2 terminate <instance-id>" 1
      fi
      ec2_terminate "$1"
      ;;
    *)
      log_error "Unknown ec2 command: $cmd" 1
      show_ec2_help
      ;;
  esac
}

function execute_script() {
  # Execute a script with the given name and arguments
  local script_name="$1"
  shift
  local args=("$@")
  local script_dir="$SCRIPT_DIR/modules/ec2"
  if ! check_directory "$script_dir"; then
    exit 1
  fi
  if [ ! -f "$script_dir/$script_name.sh" ]; then
    log_error "$script_name.sh script not found" 1
  fi
  if ! bash "$script_dir/$script_name.sh" "${args[@]}" | tee -a "$LOG_FILE"; then
    log_error "Failed to execute $script_name.sh" 1
  fi
}

function run_ec2_script() {
  # Common function to handle script execution and error logging
  local script_name="$1"
  shift
  local args=("$@")
  execute_script "$script_name" "${args[@]}"
}

function ec2_create() {
  run_ec2_script "create"
}

function ec2_list() {
  run_ec2_script "list"
}

function ec2_terminate() {
  # Input validation for instance-id
  local instance_id="$1"
  if [[ -z "$instance_id" ]]; then
    log_error "Usage: meshram ec2 terminate <instance-id>" 1
  fi
  run_ec2_script "terminate" "$instance_id"
}
```
