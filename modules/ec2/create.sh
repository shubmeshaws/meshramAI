```bash
function handle_aws_error() {
  local OUTPUT="$1"
  local RETURN_CODE="$2"

  if [ $RETURN_CODE -ne 0 ]; then
    echo "Error: Failed to execute AWS command with return code $RETURN_CODE"
    case "$OUTPUT" in
      *InvalidClientTokenId*)
        echo "  - Invalid AWS credentials: $OUTPUT. Please check your AWS access key ID and secret access key."
        ;;
      *AuthFailure*)
        echo "  - Authentication failure: $OUTPUT. Please check your AWS credentials and try again."
        ;;
      *InvalidParameter*)
        echo "  - Invalid parameter: $OUTPUT. Please check the parameters."
        ;;
      *UnauthorizedOperation*)
        echo "  - Unauthorized operation: $OUTPUT. Please check your IAM permissions and try again."
        ;;
      *)
        echo "  - Unknown error: $OUTPUT. Please check the AWS CLI output for more information."
        ;;
    esac
    return $RETURN_CODE
  fi
}

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
  handle_aws_error "$OUTPUT" $RETURN_CODE
  if [ $RETURN_CODE -eq 0 ]; then
    echo "$OUTPUT"
  fi
}
```
