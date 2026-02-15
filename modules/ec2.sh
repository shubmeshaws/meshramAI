```bash
function check_directory() {
  # Check if directory exists and is writable, and create if it does not exist
  local dir="$1"
  if [ -d "$dir" ] && [ -w "$dir" ]; then
    return 0
  elif [ -e "$dir" ]; then
    log_error "Directory $dir is not a directory or is not writable" 1
    return 1
  else
    if mkdir -p "$dir" 2>/dev/null; then
      if [ ! -d "$dir" ] || [ ! -w "$dir" ]; then
        log_error "Directory $dir is not a directory or is not writable after creation" 1
        return 1
      fi
    else
      log_error "Failed to create directory: $dir" 1
    fi
  fi
  return 0
}
```
