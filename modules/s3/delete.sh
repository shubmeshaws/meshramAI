```bash
validate_regions_conf() {
  if ! awk -F= '{if (NF != 2 || $1 == "" || $2 == "") {print "[ERROR] Invalid regions.conf format. Each line must be in the format 'region=endpoint' and both region and endpoint must be non-empty"; exit 1}}' "$SCRIPT_DIR/regions.conf"; then
    echo "Validation of regions.conf failed"
    exit 1
  fi
}

validate_regions_conf || exit 1
```
