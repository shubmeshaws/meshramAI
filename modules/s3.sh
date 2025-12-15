```bash
function log() {
  local level="$1"
  local message="$2"
  echo "[$level] $message" | tee -a "$LOG_FILE"
}

function handle_error() {
  local exit_code=$1
  local command="$2"
  log "ERROR" "Failed to execute command '$command' (exit code: $exit_code)"
  exit $exit_code
}

function validate_input() {
  if [[ -z "$1" || -z "$2" ]]; then
    log "ERROR" "Usage: meshram s3 create <bucket-name> <region> [public|private]"
    exit 1
  fi
  if [[ "$3" != "public" && "$3" != "private" && -n "$3" ]]; then
    log "ERROR" "Invalid ACL: $3. Only 'public' or 'private' are allowed"
    exit 1
  fi
}

function s3_create() {
  validate_input "$1" "$2" "$3"
  local bucket_name="$1"
  local input_region="$2"
  local acl="${3:-private}" # default to private
  local region=$(map_region_name "$input_region")
  log "INFO" "Creating bucket '$bucket_name' in region '$region' with ACL '$acl'..."
  if ! bash "$SCRIPT_DIR/modules/s3/create.sh" "$bucket_name" "$region" "$acl" | tee -a "$LOG_FILE"; then
    handle_error $? "s3 create"
  fi
}

function s3_list() {
  log "INFO" "Listing S3 buckets..."
  if ! bash "$SCRIPT_DIR/modules/s3/list.sh" | tee -a "$LOG_FILE"; then
    handle_error $? "s3 list"
  fi
}

function s3_delete() {
  if [[ -z "$1" ]]; then
    log "ERROR" "Usage: meshram s3 delete <bucket-name>"
    exit 1
  fi
  log "INFO" "Deleting bucket '$1'..."
  if ! bash "$SCRIPT_DIR/modules/s3/delete.sh" "$1" | tee -a "$LOG_FILE"; then
    handle_error $? "s3 delete"
  fi
}

function main() {
  case $1 in
    create)
      shift
      s3_create "$@"
      ;;
    list)
      shift
      s3_list
      ;;
    delete)
      shift
      s3_delete "$@"
      ;;
    *)
      log "ERROR" "Unknown command: $1"
      exit 1
      ;;
  esac
}

main "$@"
```
