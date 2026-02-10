```bash
function check_directory() {
  # Check if directory exists and is writable, and create if it does not exist
  local dir="$1"
  if mkdir -p "$dir" 2>/dev/null; then
    if [ -d "$dir" ] && [ -w "$dir" ]; then
      return 0
    fi
  fi
  log_error "Failed to create or write to directory: $dir" 1
  return 1
}
```
