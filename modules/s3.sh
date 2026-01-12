```bash
function validate_region() {
  local region="$1"
  if ! aws ec2 describe-regions --region "$region" --output text &> /dev/null; then
    local valid_regions=$(aws ec2 describe-regions --output text | awk '{print $2}')
    log "ERROR" "Invalid region: $region. Supported regions: $valid_regions"
    exit 1
  fi
}
```
