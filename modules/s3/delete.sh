```bash
validate_regions_conf() {
  awk -F= '{if (NF != 2 || $1 == "" || $2 == "") {print "[ERROR] Invalid regions.conf format. Each line must be in the format 'region=endpoint' and both region and endpoint must be non-empty"; exit 1}}' "$SCRIPT_DIR/regions.conf" &> /dev/null
}

validate_regions_conf || exit 1
```
