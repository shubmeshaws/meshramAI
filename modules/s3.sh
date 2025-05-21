#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -L "$SOURCE" ]; do
  DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"

function show_s3_help() {
  echo "S3 service commands:"
  echo "  meshram s3 create <bucket-name> <region> [public|private] 	- Create S3 bucket"
  echo "  meshram s3 list                 				- List all S3 buckets"
  echo "  meshram s3 delete <bucket-name> 				- Delete an S3 bucket"
}

function map_region_name() {
  local input_region="$1"
  declare -A regions_map
  while IFS='=' read -r key value; do
    [[ -z "$key" || "$key" =~ ^# ]] && continue
    regions_map["$key"]="$value"
  done < "$SCRIPT_DIR/regions.conf"

  if [[ -n "${regions_map[$input_region]}" ]]; then
    echo "${regions_map[$input_region]}"
  else
    echo "$input_region"
  fi
}

function s3_handler() {
  local cmd="$1"
  shift
  case "$cmd" in
    help|"")
      show_s3_help
      ;;
    create)
      s3_create "$@"
      ;;
    list)
      s3_list
      ;;
    delete)
      s3_delete "$@"
      ;;
    *)
      echo "[ERROR] Unknown s3 command: $cmd"
      show_s3_help
      ;;
  esac
}

function s3_create() {
  if [[ -z "$1" || -z "$2" ]]; then
    echo "[ERROR] Usage: meshram s3 create <bucket-name> <region> [public|private]"
    exit 1
  fi
  local bucket_name="$1"
  local input_region="$2"
  local acl="${3:-private}" # default to private
  local region=$(map_region_name "$input_region")
  echo "[INFO] Creating bucket '$bucket_name' in region '$region' with ACL '$acl'..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/s3/create.sh" "$bucket_name" "$region" "$acl" | tee -a "$LOG_FILE"
}

function s3_list() {
  echo "[INFO] Listing S3 buckets..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/s3/list.sh" | tee -a "$LOG_FILE"
}

function s3_delete() {
  if [[ -z "$1" ]]; then
    echo "[ERROR] Usage: meshram s3 delete <bucket-name>"
    exit 1
  fi
  echo "[INFO] Deleting bucket '$1'..." | tee -a "$LOG_FILE"
  bash "$SCRIPT_DIR/modules/s3/delete.sh" "$1" | tee -a "$LOG_FILE"
}

