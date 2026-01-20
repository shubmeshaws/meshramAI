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
    echo "Error: Failed to describe images"
    case "$OUTPUT" in
      *InvalidClientTokenId*)
        echo "  - Invalid AWS credentials: $OUTPUT"
        ;;
      *AuthFailure*)
        echo "  - Authentication failure: $OUTPUT"
        ;;
      *)
        echo "  - Unknown error: $OUTPUT"
        ;;
    esac
    return $RETURN_CODE
  fi
  echo "$OUTPUT"
}
```
