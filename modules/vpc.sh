#!/bin/bash

#bash "$SCRIPT_DIR/modules/vpc/create.sh"

function show_vpc_help() {
  echo "VPC service commands:"
  echo "  meshram vpc create                 - Create a VPC with subnets and NAT"
  echo "  meshram vpc list                   - List VPCs"
  echo "  meshram vpc delete <vpc-id>       - Delete a VPC"
}

function vpc_handler() {
  local cmd="$1"
  shift
  case "$cmd" in
    help|"")
      show_vpc_help
      ;;
    create)
      vpc_create
      ;;
    list)
      vpc_list
      ;;
    delete)
      vpc_delete "$@"
      ;;
    *)
      echo "[ERROR] Unknown vpc command: $cmd"
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
  if [[ -z "$vpc_id" ]]; then
    echo "[ERROR] Usage: meshram vpc delete <vpc-id>"
    exit 1
  fi
  echo "[INFO] Deleting VPC $vpc_id..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/vpc/delete.sh" "$vpc_id" | tee -a "$LOG_FILE"
}

