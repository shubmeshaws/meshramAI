```bash
function validate_region() {
  local region="$1"
  local valid_region=$(aws ec2 describe-regions --query "Regions[?RegionName=='$region']" --output text)
  if [ $? -ne 0 ]; then
    log "ERROR" "Failed to validate region: $region. Error: $(aws ec2 describe-regions --query "Regions[?RegionName=='$region']" --output text 2>&1)"
    exit 1
  fi
  if [ -z "$valid_region" ]; then
    local valid_regions=$(aws ec2 describe-regions --query 'Regions[].RegionName' --output text)
    log "ERROR" "Invalid region: $region. Supported regions: $valid_regions"
    exit 1
  fi
}
```
