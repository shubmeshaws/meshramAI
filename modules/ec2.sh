```bash
function check_directory() {
  # Check if directory exists and is writable, and create if it does not exist
  local dir="$1"
  if [ ! -d "$dir" ]; then
    if ! mkdir -p "$dir" 2>/dev/null; then
      log_error "Failed to create directory: $dir. Error: $?" 1
      return 1
    fi
  elif [ ! -w "$dir" ]; then
    log_error "Directory $dir is not writable. Permission denied" 1
    return 1
  fi
  return 0
}
```
