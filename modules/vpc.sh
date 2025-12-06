```bash
#!/bin/bash

#bash "$SCRIPT_DIR/modules/vpc/create.sh"

function show_vpc_help() {
  echo "VPC service commands:"
  echo "  meshram vpc create                 - Create a VPC with subnets and NAT"
  echo "  meshram vpc list                   - List VPCs"
  echo "  meshram vpc delete <vpc-id>       - Delete a VPC"
}

function vpc_handler() {
  if [[ -z "$1" ]]; then
    echo "[ERROR] No command provided. Please use one of the following commands: create, list, delete"
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
      if [[ -n "$1" ]]; then
        echo "[ERROR] Usage: meshram vpc create"
        show_vpc_help
        return 1
      fi
      vpc_create
      ;;
    list)
      if [[ -n "$1" ]]; then
        echo "[ERROR] Usage: meshram vpc list"
        show_vpc_help
        return 1
      fi
      vpc_list
      ;;
    delete)
      if [[ -z "$1" ]]; then
        echo "[ERROR] Usage: meshram vpc delete <vpc-id>"
        show_vpc_help
        return 1
      fi
      vpc_delete "$@"
      ;;
    *)
      echo "[ERROR] Unknown vpc command: $cmd. Please use one of the following commands: create, list, delete"
      show_vpc_help
      ;;
  esac
}

function vpc_create() {
  echo "[INFO] Creating VPC..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/vpc/create.sh" | tee -a "$LOG_FILE"
}

function vpc_list() {
  echo "[INFO] Listing VPCs..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/vpc/list.sh" | tee -a "$LOG_FILE"
}

function vpc_delete() {
  local vpc_id="$1"
  if ! [[ "$vpc_id" =~ ^vpc-[a-z0-9]{17}$ ]]; then
    echo "[ERROR] Invalid VPC ID: $vpc_id. Please use a valid VPC ID."
    show_vpc_help
    return 1
  fi
  echo "[INFO] Deleting VPC $vpc_id..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/vpc/delete.sh" "$vpc_id" | tee -a "$LOG_FILE"
}
```
