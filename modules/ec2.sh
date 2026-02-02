```bash
function check_directory() {
  # Check if directory exists, is writable, and create if it does not exist
  local dir="$1"
  if mkdir -p "$dir" 2>/dev/null; then
    if [ -d "$dir" ] && [ -w "$dir" ]; then
      return 0
    else
      log_error "Directory is not writable or does not exist: $dir" 1
      return 1
    fi
  else
    log_error "Failed to create directory: $dir. Error: $?" 1
    return 1
  fi
}
```
