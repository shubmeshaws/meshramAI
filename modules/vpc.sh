```bash
#!/bin/bash

# Check if required variables are set
if [ -z "$LOG_FILE" ]; then
  echo "[ERROR] LOG_FILE variable is not set."
  exit 1
fi

if [ -z "$SCRIPT_DIR" ]; then
  echo "[ERROR] SCRIPT_DIR variable is not set."
  exit 1
fi

# Check if script directory and log file exist
if [ ! -d "$SCRIPT_DIR" ]; then
  echo "[ERROR] Script directory '$SCRIPT_DIR' does not exist."
  exit 1
fi

if [ ! -f "$LOG_FILE" ]; then
  touch "$LOG_FILE" || { echo "[ERROR] Unable to create log file '$LOG_FILE'."; exit 1; }
fi

function log_info() {
  local message="$1"
  echo "[INFO] $message" | tee -a "$LOG_FILE"
}

function log_error() {
  local message="$1"
  echo "[ERROR] $message" | tee -a "$LOG_FILE"
}

function show_vpc_help() {
  echo "VPC service commands:"
  echo "  meshram vpc create                 - Create a VPC with subnets and NAT"
  echo "  meshram vpc list                   - List VPCs"
  echo "  meshram vpc delete <vpc-id>       - Delete a VPC"
}

function validate_vpc_id() {
  local vpc_id="$1"
  if ! [[ "$vpc_id" =~ ^vpc-[a-z0-9]{17}$ ]]; then
    log_error "Invalid VPC ID: $vpc_id. Please use a valid VPC ID."
    show_vpc_help
    return 1
  fi
}

function vpc_handler() {
  if [[ -z "$1" ]]; then
    log_error "No command provided. Please use one of the following commands: create, list, delete"
    show_vpc_help
    return 1
  fi

  local cmd="$1"
  shift
  case "$cmd" in
    help|"")
      show_vpc_help
      ;;
    create)
      if [[ $# -ne 0 ]]; then
        log_error "Usage: meshram vpc create"
        show_vpc_help
        return 1
      fi
      vpc_create
      ;;
    list)
      if [[ $# -ne 0 ]]; then
        log_error "Usage: meshram vpc list"
        show_vpc_help
        return 1
      fi
      vpc_list
      ;;
    delete)
      if [[ $# -ne 1 ]]; then
        log_error "Usage: meshram vpc delete <vpc-id>"
        show_vpc_help
        return 1
      fi
      if ! validate_vpc_id "$1"; then
        return 1
      fi
      vpc_delete "$@"
      ;;
    *)
      log_error "Unknown vpc command: $cmd. Please use one of the following commands: create, list, delete"
      show_vpc_help
      ;;
  esac
}

function vpc_create() {
  log_info "Creating VPC..."
  if ! bash "$SCRIPT_DIR/modules/vpc/create.sh" | tee -a "$LOG_FILE"; then
    log_error "Failed to create VPC. Please check the logs for more information."
    return 1
  fi
}

function vpc_list() {
  log_info "Listing VPCs..."
  if ! bash "$SCRIPT_DIR/modules/vpc/list.sh" | tee -a "$LOG_FILE"; then
    log_error "Failed to list VPCs. Please check the logs for more information."
    return 1
  fi
}

function vpc_delete() {
  local vpc_id="$1"
  log_info "Deleting VPC $vpc_id..."
  if ! bash "$SCRIPT_DIR/modules/vpc/delete.sh" "$vpc_id" | tee -a "$LOG_FILE"; then
    log_error "Failed to delete VPC $vpc_id. Please check the logs for more information."
    return 1
  fi
}

function main() {
  vpc_handler "$@"
}

main "$@"
```
