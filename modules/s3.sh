```bash
function validate_region() {
  local region="$1"
  local valid_regions=$(aws ec2 describe-regions --output text | awk '{print $2}')
  if [[ ! " ${valid_regions} " =~ " ${region} " ]]; then
    log "ERROR" "Invalid region: $region. Supported regions: $valid_regions"
    exit 1
  fi
}
```
