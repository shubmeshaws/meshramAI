```bash
function check_directory() {
  # Check if directory exists and is writable, and create if it does not exist
  local dir="$1"
  if [ ! -d "$dir" ]; then
    if ! mkdir -p "$dir" 2>/dev/null; then
      log_error "Failed to create directory: $dir. Error: $?" 1
      return 1
    fi
  fi
  # Check again after creation attempt to handle potential race conditions
  if [ ! -d "$dir" ]; then
    log_error "Directory $dir does not exist after creation attempt" 1
    return 1
  elif [ ! -w "$dir" ]; then
    log_error "Directory $dir is not writable. Permission denied" 1
    return 1
  fi
  return 0
}
```
