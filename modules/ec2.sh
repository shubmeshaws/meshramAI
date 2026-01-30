```bash
function check_directory() {
  # Check if directory exists, is writable, and create if it does not exist
  local dir="$1"
  if mkdir -p "$dir" && [ -d "$dir" ] && [ -w "$dir" ]; then
    return 0
  else
    log_error "Failed to create or access directory: $dir. Error: $?" 1
    return 1
  fi
}
```
