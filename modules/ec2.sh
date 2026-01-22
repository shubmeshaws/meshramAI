```bash
function check_directory() {
  # Check if directory exists and is writable, create if it does not exist
  local dir="$1"
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir" || { log_error "Failed to create directory: $dir. Error: $?"; return 1; }
  fi
  if [ ! -w "$dir" ]; then
    log_error "Directory is not writable: $dir" 1
    return 1
  fi
  return 0
}
```
