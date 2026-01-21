```bash
VPC_ID_PATTERN="^vpc-[a-z0-9]{17}$"
INVALID_VPC_ID_ERROR_MESSAGE="Invalid VPC ID: %s. A valid VPC ID should be in the format 'vpc-xxxxxxxxxxxxxxxxx' where 'x' is a lowercase letter or number. Please check the ID and try again. Example of a valid VPC ID: 'vpc-1234567890abcdef'"
EXIT_ON_ERROR=1

function validate_vpc_id() {
  local vpc_id="$1"
  if [ -z "$vpc_id" ]; then
    return 1
  fi
  if ! [[ "$vpc_id" =~ $VPC_ID_PATTERN ]]; then
    return 1
  fi
  return 0
}

function show_vpc_help() {
  echo "Valid VPC ID format: vpc-xxxxxxxxxxxxxxxxx"
  echo "Where 'x' is a lowercase letter or number."
  echo "Example: vpc-1234567890abcdef"
}

function validate_and_handle_vpc_id() {
  local vpc_id="$1"
  if [ -z "$vpc_id" ]; then
    echo "ERROR: VPC ID is required." >&2
    show_vpc_help
    exit $EXIT_ON_ERROR
  fi
  if ! validate_vpc_id "$vpc_id"; then
    local error_message=$(printf "$INVALID_VPC_ID_ERROR_MESSAGE" "$vpc_id")
    echo "ERROR: $error_message" >&2
    show_vpc_help
    exit $EXIT_ON_ERROR
  fi
}

function main() {
  local vpc_id="$1"
  validate_and_handle_vpc_id "$vpc_id"
}

main "$1"
```
