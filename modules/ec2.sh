```bash
#!/bin/bash

#bash "$SCRIPT_DIR/modules/ec2/create.sh"

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

function ec2_create() {
  echo "[INFO] Launching EC2 instance..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/ec2/create.sh" | tee -a "$LOG_FILE"
}

function ec2_list() {
  echo "[INFO] Listing EC2 instances..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/ec2/list.sh" | tee -a "$LOG_FILE"
}

function ec2_terminate() {
  local instance_id="$1"
  if [[ -z "$instance_id" ]]; then
    echo "[ERROR] Usage: meshram ec2 terminate <instance-id>"
    exit 1
  fi
  echo "[INFO] Terminating EC2 instance $instance_id..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/ec2/terminate.sh" "$instance_id" | tee -a "$LOG_FILE"
}
```
