```bash
#!/bin/bash

# Check if SCRIPT_DIR is set
if [ -z "$SCRIPT_DIR" ]; then
  log_error "SCRIPT_DIR variable is not set"
  exit 1
fi

# Check if LOG_FILE is set
if [ -z "$LOG_FILE" ]; then
  echo "[ERROR] LOG_FILE variable is not set"
  exit 1
fi

function log_error() {
  # Log error message and exit
  echo "[ERROR] $1" | tee -a "$LOG_FILE"
  exit 1
}

function log_info() {
  # Log info message
  echo "[INFO] $1" | tee -a "$LOG_FILE"
}

function check_directory() {
  # Check if directory exists and is writable
  local dir="$1"
  if [ ! -d "$dir" ]; then
    log_error "Directory does not exist: $dir"
  fi
  if [ ! -w "$dir" ]; then
    log_error "Directory is not writable: $dir"
  fi
}

# Check if SCRIPT_DIR and LOG_FILE directories exist and are writable
check_directory "$SCRIPT_DIR"
check_directory "$(dirname "$LOG_FILE")"

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
        log_error "Usage: meshram ec2 terminate <instance-id>"
      fi
      ec2_terminate "$1"
      ;;
    *)
      log_error "Unknown ec2 command: $cmd"
      show_ec2_help
      ;;
  esac
}

function execute_script() {
  # Execute a script with the given name and arguments
  local script_name="$1"
  shift
  local args=("$@")
  if [ ! -f "$SCRIPT_DIR/modules/ec2/$script_name.sh" ]; then
    log_error "$script_name.sh script not found"
  fi
  if ! bash "$SCRIPT_DIR/modules/ec2/$script_name.sh" "${args[@]}" | tee -a "$LOG_FILE"; then
    log_error "Failed to execute $script_name.sh"
  fi
}

function ec2_create() {
  execute_script "create"
}

function ec2_list() {
  execute_script "list"
}

function ec2_terminate() {
  # Input validation for instance-id
  local instance_id="$1"
  if [[ -z "$instance_id" ]]; then
    log_error "Usage: meshram ec2 terminate <instance-id>"
  fi
  execute_script "terminate" "$instance_id"
}
```
