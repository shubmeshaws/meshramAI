```bash
function describe_images() {
  local OWNER="$1"
  local FILTERS="$2"
  local REGION="$3"

  # Input validation
  if [ -z "$OWNER" ] || [ -z "$FILTERS" ] || [ -z "$REGION" ]; then
    local ERROR_MESSAGE="Error: OWNER, FILTERS, and REGION are required parameters"
    echo "$ERROR_MESSAGE"
    return 1
  fi

  local OUTPUT
  OUTPUT=$(aws ec2 describe-images --owners "$OWNER" --filters "$FILTERS" "Name=state,Values=available" --region "$REGION" --query 'Images[*].[ImageId,CreationDate]' --output text 2>&1)
  local RETURN_CODE=$?
  if [ $RETURN_CODE -ne 0 ]; then
    local INVALID_CREDENTIALS_ERROR="Error: Invalid AWS credentials"
    local AUTH_FAILURE_ERROR="Error: Authentication failure"
    local GENERIC_ERROR="Error: Failed to describe images - $OUTPUT"
    if echo "$OUTPUT" | grep -q "InvalidClientTokenId"; then
      echo "$INVALID_CREDENTIALS_ERROR"
    elif echo "$OUTPUT" | grep -q "AuthFailure"; then
      echo "$AUTH_FAILURE_ERROR"
    else
      echo "$GENERIC_ERROR"
    fi
    return $RETURN_CODE
  fi
  echo "$OUTPUT"
}
```
