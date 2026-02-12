```bash
VPC_ID_PREFIX="vpc-"
VPC_ID_CHAR_SET="[a-z0-9]"
INVALID_VPC_ID_ERROR_MESSAGE="Invalid VPC ID: %s. A valid VPC ID should be in the format '%s%s' where '%s' is a lowercase letter or number. Please check the ID and try again. Example of a valid VPC ID: '%s1234567890abcdef'"
EXIT_ON_MISSING_VPC_ID=10
EXIT_ON_INVALID_VPC_ID=20
EXIT_ON_INVALID_INPUT_TYPE=30
EXIT_ON_WRONG_ARGUMENTS=40
VPC_ID_LENGTH=16  # corrected length without prefix

function generate_error_message() {
  local vpc_id="$1"
  printf "$INVALID_VPC_ID_ERROR_MESSAGE" "$vpc_id" "$VPC_ID_PREFIX" "${VPC_ID_CHAR_SET}" "${VPC_ID_CHAR_SET}" "$VPC_ID_PREFIX"
}

function validate_vpc_id() {
  local vpc_id="$1"
  if [ -z "$vpc_id" ]; then
    echo "VPC ID is empty" >&2
    return $EXIT_ON_MISSING_VPC_ID
  elif ! [[ "$vpc_id" =~ ^[a-zA-Z0-9-]+$ ]]; then
    echo "VPC ID contains invalid characters" >&2
    return $EXIT_ON_INVALID_INPUT_TYPE
  elif ! [[ "$vpc_id" =~ ^${VPC_ID_PREFIX}[${VPC_ID_CHAR_SET}]{${VPC_ID_LENGTH}}$ ]]; then
    local error_message=$(generate_error_message "$vpc_id")
    echo "$error_message" >&2
    return $EXIT_ON_INVALID_VPC_ID
  fi
  return 0
}

function show_vpc_help() {
  echo "Valid VPC ID format: ${VPC_ID_PREFIX}xxxxxxxxxxxxxxxxx"
  echo "Where 'x' is a lowercase letter or number."
  echo "Example: ${VPC_ID_PREFIX}1234567890abcdef"
}

function handle_error() {
  local error_type="$1"
  local vpc_id="$2"
  case "$error_type" in
    missing)
      echo "ERROR: VPC ID is required." >&2
      ;;
    invalid)
      local error_message=$(generate_error_message "$vpc_id")
      echo "ERROR: $error_message" >&2
      ;;
    invalid_type)
      echo "ERROR: Invalid input type. VPC ID must be a string containing only letters, numbers, and hyphens." >&2
      ;;
    wrong_arguments)
      echo "ERROR: Exactly one VPC ID is required as an argument." >&2
      ;;
  esac
  show_vpc_help
  case "$error_type" in
    missing) exit $EXIT_ON_MISSING_VPC_ID ;;
    invalid) exit $EXIT_ON_INVALID_VPC_ID ;;
    invalid_type) exit $EXIT_ON_INVALID_INPUT_TYPE ;;
    wrong_arguments) exit $EXIT_ON_WRONG_ARGUMENTS ;;
  esac
}

function validate_and_handle_vpc_id() {
  local vpc_id="$1"
  local exit_code
  validate_vpc_id "$vpc_id"
  exit_code=$?
  if [ $exit_code -eq $EXIT_ON_MISSING_VPC_ID ]; then
    handle_error "missing"
  elif [ $exit_code -eq $EXIT_ON_INVALID_VPC_ID ]; then
    handle_error "invalid" "$vpc_id"
  elif [ $exit_code -eq $EXIT_ON_INVALID_INPUT_TYPE ]; then
    handle_error "invalid_type"
  fi
}

function main() {
  if [ $# -ne 1 ]; then
    handle_error "wrong_arguments"
  fi
  local vpc_id="$1"
  validate_and_handle_vpc_id "$vpc_id"
}

main "$1"
```
