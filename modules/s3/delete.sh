```bash
validate_regions_conf() {
  if ! awk -F= '{if (NF != 2 || $1 == "" || $2 == "") {print "[ERROR] Invalid regions.conf format at line " NR ": "" $0 "". Each line must be in the format 'region=endpoint' and both region and endpoint must be non-empty"; exit 1}}' "$SCRIPT_DIR/regions.conf"; then
    echo "Error: Validation of regions.conf failed. Please check the file format and ensure each line is in the format 'region=endpoint' with non-empty values."
    exit 1
  fi
}

if ! validate_regions_conf; then
  exit 1
fi
```
