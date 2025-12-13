```bash
#!/bin/bash

# Check if SCRIPT_DIR is set
if [ -z "$SCRIPT_DIR" ]; then
  echo "[ERROR] SCRIPT_DIR variable is not set"
  exit 1
fi

# Check if LOG_FILE is set
if [ -z "$LOG_FILE" ]; then
  echo "[ERROR] LOG_FILE variable is not set"
  exit 1
fi

function show_ec2_help() {
  echo "EC2 service commands:"
  echo "  meshram ec2 create                 - Launch an EC2 instance"
  echo "  meshram ec2 list                   - List EC2 instances"
  echo "  meshram ec2 terminate <instance-id> - Terminate an EC2 instance"
}

function ec2_handler() {
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
      if [ $# -ne 1 ]; then
        echo "[ERROR] Usage: meshram ec2 terminate <instance-id>"
        exit 1
      fi
      ec2_terminate "$1"
      ;;
    *)
      echo "[ERROR] Unknown ec2 command: $cmd"
      show_ec2_help
      ;;
  esac
}

function execute_script() {
  local script_name="$1"
  shift
  local args=("$@")
  if [ ! -f "$SCRIPT_DIR/modules/ec2/$script_name.sh" ]; then
    echo "[ERROR] $script_name.sh script not found" | tee -a "$LOG_FILE"
    exit 1
  fi
  if ! bash "$SCRIPT_DIR/modules/ec2/$script_name.sh" "${args[@]}" | tee -a "$LOG_FILE"; then
    echo "[ERROR] Failed to execute $script_name.sh" | tee -a "$LOG_FILE"
    exit 1
  fi
}

function ec2_create() {
  execute_script "create"
}

function ec2_list() {
  execute_script "list"
}

function ec2_terminate() {
  local instance_id="$1"
  if [[ -z "$instance_id" ]]; then
    echo "[ERROR] Usage: meshram ec2 terminate <instance-id>"
    exit 1
  fi
  execute_script "terminate" "$instance_id"
}
```
