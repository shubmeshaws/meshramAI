```bash
function check_directory() {
  # Check if directory exists and is writable, create if it does not exist
  local dir="$1"
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir" || log_error "Failed to create directory: $dir. Error: $?" 1
  fi
  [ -w "$dir" ] || log_error "Directory is not writable: $dir" 1
  return 0
}
```
