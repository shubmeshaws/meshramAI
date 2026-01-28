```bash
function check_directory() {
  # Check if directory exists, is writable, and create if it does not exist
  local dir="$1"
  mkdir -p "$dir" || { log_error "Failed to create directory: $dir. Error: $?"; return 1; }
  if [ ! -d "$dir" ] || [ ! -w "$dir" ]; then
    log_error "Directory is not writable or does not exist: $dir" 1
    return 1
  fi
  return 0
}
```
