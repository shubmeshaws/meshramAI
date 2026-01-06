```bash
function describe_images() {
  local OWNER="$1"
  local FILTERS="$2"
  local REGION="$3"
  local OUTPUT
  OUTPUT=$(aws ec2 describe-images --owners "$OWNER" --filters "$FILTERS" "Name=state,Values=available" --region "$REGION" --query 'Images[*].[ImageId,CreationDate]' --output text 2>&1)
  local RETURN_CODE=$?
  if [ $RETURN_CODE -ne 0 ]; then
    handle_describe_images_error "$OUTPUT" $RETURN_CODE
    return $RETURN_CODE
  fi
  echo "$OUTPUT"
}
```
