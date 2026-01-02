```bash
function validate_region() {
  local region="$1"
  local valid_regions=$(aws ec2 describe-regions --query 'Regions[].RegionName' --output text)
  if [[ ! " ${valid_regions[@]} " =~ " $region " ]]; then
    log "ERROR" "Invalid region: $region. Supported regions: $valid_regions"
    exit 1
  fi
}
```
Note: This improved code assumes that the AWS CLI is installed and configured properly on the system. If not, you may need to add additional error handling or installation instructions.
