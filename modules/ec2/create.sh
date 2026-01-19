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
    case "$OUTPUT" in
      *InvalidClientTokenId*)
        echo "Error: Invalid AWS credentials"
        ;;
      *AuthFailure*)
        echo "Error: Authentication failure"
        ;;
      *)
        echo "Error: Failed to describe images - $OUTPUT"
        ;;
    esac
    return $RETURN_CODE
  fi
  echo "$OUTPUT"
}
```
