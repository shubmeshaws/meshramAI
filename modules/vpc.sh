```bash
VPC_ID_PATTERN="^vpc-[a-z0-9]{17}$"

function validate_vpc_id() {
  local vpc_id="$1"
  if ! [[ "$vpc_id" =~ $VPC_ID_PATTERN ]]; then
    log_error "Invalid VPC ID: $vpc_id. A valid VPC ID should be in the format 'vpc-xxxxxxxxxxxxxxxxx' where 'x' is a lowercase letter or number. Please check the ID and try again."
    show_vpc_help
    return 1
  fi
}
```
