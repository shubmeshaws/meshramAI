```bash
function log() {
  local level="$1"
  local message="$2"
  if [ -z "$LOG_FILE" ]; then
    echo "ERROR: LOG_FILE variable is not set" >&2
    exit 1
  fi
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

function validate_region() {
  local region="$1"
  local valid_regions=("us-east-1" "us-west-2" "eu-west-1" "ap-northeast-1" "ap-southeast-1")
  if [[ ! " ${valid_regions[@]} " =~ " $region " ]]; then
    log "ERROR" "Invalid region: $region. Supported regions: ${valid_regions[@]}"
    exit 1
  fi
}

function check_script_dir() {
  if [ ! -d "$SCRIPT_DIR" ]; then
    log "ERROR" "Script directory '$SCRIPT_DIR' does not exist"
    exit 1
  fi
  if [ ! -d "$SCRIPT_DIR/modules/s3" ]; then
    log "ERROR" "S3 script directory '$SCRIPT_DIR/modules/s3' does not exist"
    exit 1
  fi
  if [ ! -f "$SCRIPT_DIR/modules/s3/create.sh" ] || [ ! -f "$SCRIPT_DIR/modules/s3/list.sh" ] || [ ! -f "$SCRIPT_DIR/modules/s3/delete.sh" ]; then
    log "ERROR" "One or more required S3 scripts are missing in '$SCRIPT_DIR/modules/s3'"
    exit 1
  fi
}

function map_region_name() {
  local input_region="$1"
  case $input_region in
    us-east)
      echo "us-east-1"
      ;;
    us-west)
      echo "us-west-2"
      ;;
    eu-west)
      echo "eu-west-1"
      ;;
    ap-northeast)
      echo "ap-northeast-1"
      ;;
    ap-southeast)
      echo "ap-southeast-1"
      ;;
    *)
      log "ERROR" "Invalid region name: $input_region. Supported region names: us-east, us-west, eu-west, ap-northeast, ap-southeast"
      exit 1
      ;;
  esac
}

function exit_code_1() {
  log "ERROR" "Usage: meshram s3 <command> [options]"
  exit 1
}

function exit_code_127() {
  log "ERROR" "Command not found"
  exit 127
}

function s3_create() {
  validate_input "$1" "$2" "$3"
  local bucket_name="$1"
  local input_region="$2"
  local acl="${3:-private}" # default to private
  local region=$(map_region_name "$input_region")
  validate_region "$region"
  log "INFO" "Creating bucket '$bucket_name' in region '$region' with ACL '$acl'..."
  if ! bash "$SCRIPT_DIR/modules/s3/create.sh" "$bucket_name" "$region" "$acl" | tee -a "$LOG_FILE"; then
    case $? in
      1) exit_code_1 ;;
      127) exit_code_127 ;;
      *) handle_error $? "s3 create" ;;
    esac
  fi
}

function s3_list() {
  log "INFO" "Listing S3 buckets..."
  if ! bash "$SCRIPT_DIR/modules/s3/list.sh" | tee -a "$LOG_FILE"; then
    case $? in
      1) exit_code_1 ;;
      127) exit_code_127 ;;
      *) handle_error $? "s3 list" ;;
    esac
  fi
}

function s3_delete() {
  if [[ -z "$1" ]]; then
    log "ERROR" "Usage: meshram s3 delete <bucket-name>"
    exit 1
  fi
  log "INFO" "Deleting bucket '$1'..."
  if ! bash "$SCRIPT_DIR/modules/s3/delete.sh" "$1" | tee -a "$LOG_FILE"; then
    case $? in
      1) exit_code_1 ;;
      127) exit_code_127 ;;
      *) handle_error $? "s3 delete" ;;
    esac
  fi
}

function check_environment() {
  if [ -z "$LOG_FILE" ]; then
    echo "ERROR: LOG_FILE environment variable is not set" >&2
    exit 1
  fi
  if [ -z "$SCRIPT_DIR" ]; then
    echo "ERROR: SCRIPT_DIR environment variable is not set" >&2
    exit 1
  fi
}

function main() {
  check_environment
  check_script_dir
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
