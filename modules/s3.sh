```bash
function validate_region() {
  local region="$1"
  local regions_output=$(aws ec2 describe-regions --output text)
  if [ $? -ne 0 ]; then
    log "ERROR" "Failed to validate region: $region. Error: $regions_output"
    exit 1
  fi
  local valid_region=$(echo "$regions_output" | grep "$region")
  if [ -z "$valid_region" ]; then
    local valid_regions=$(echo "$regions_output")
    log "ERROR" "Invalid region: $region. Supported regions: $valid_regions"
    exit 1
  fi
}
```
