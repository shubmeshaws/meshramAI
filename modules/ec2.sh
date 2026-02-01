```bash
function check_directory() {
  # Check if directory exists, is writable, and create if it does not exist
  local dir="$1"
  if [ ! -d "$dir" ]; then
    if ! mkdir -p "$dir"; then
      log_error "Failed to create directory: $dir. Error: $?" 1
      return 1
    fi
  fi
  if [ ! -d "$dir" ]; then
    log_error "Directory does not exist after creation: $dir" 1
    return 1
  fi
  if [ ! -w "$dir" ]; then
    log_error "Directory is not writable: $dir" 1
    return 1
  fi
  return 0
}
```
