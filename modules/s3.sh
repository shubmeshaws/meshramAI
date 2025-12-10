```bash
function validate_input() {
  if [[ -z "$1" || -z "$2" ]]; then
    echo "[ERROR] Usage: meshram s3 create <bucket-name> <region> [public|private]"
    exit 1
  fi
  if [[ "$3" != "public" && "$3" != "private" && -n "$3" ]]; then
    echo "[ERROR] Invalid ACL: $3. Only 'public' or 'private' are allowed"
    exit 1
  fi
}

function s3_create() {
  validate_input "$1" "$2" "$3"
  local bucket_name="$1"
  local input_region="$2"
  local acl="${3:-private}" # default to private
  local region=$(map_region_name "$input_region")
  echo "[INFO] Creating bucket '$bucket_name' in region '$region' with ACL '$acl'..." | tee -a "$LOG_FILE"
  if ! bash "$SCRIPT_DIR/modules/s3/create.sh" "$bucket_name" "$region" "$acl" | tee -a "$LOG_FILE"; then
    local exit_code=$?
    echo "[ERROR] Failed to create bucket '$bucket_name' (exit code: $exit_code)" | tee -a "$LOG_FILE"
    exit $exit_code
  fi
}

function s3_list() {
  echo "[INFO] Listing S3 buckets..." | tee -a "$LOG_FILE"
  if ! bash "$SCRIPT_DIR/modules/s3/list.sh" | tee -a "$LOG_FILE"; then
    local exit_code=$?
    echo "[ERROR] Failed to list S3 buckets (exit code: $exit_code)" | tee -a "$LOG_FILE"
    exit $exit_code
  fi
}

function s3_delete() {
  if [[ -z "$1" ]]; then
    echo "[ERROR] Usage: meshram s3 delete <bucket-name>"
    exit 1
  fi
  echo "[INFO] Deleting bucket '$1'..." | tee -a "$LOG_FILE"
  if ! bash "$SCRIPT_DIR/modules/s3/delete.sh" "$1" | tee -a "$LOG_FILE"; then
    local exit_code=$?
    echo "[ERROR] Failed to delete bucket '$1' (exit code: $exit_code)" | tee -a "$LOG_FILE"
    exit $exit_code
  fi
}
```
