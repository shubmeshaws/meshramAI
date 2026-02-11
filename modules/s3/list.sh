```bash
function retry_command() {
  local command=$1
  local max_retries=$2
  local retry_count=0
  while [ $retry_count -lt $max_retries ]; do
    if output=$(timeout $TIMEOUT_SECONDS"s" $command 2>&1); then
      if echo "$output" | grep -q "Error"; then
        handle_error 0 "$output" "$command"
      else
        echo "$output"
        return
      fi
    else
      exit_code=$?
      if [ $exit_code -eq 124 ]; then
        # Handle timeout error
        handle_error $exit_code "Command timed out after $TIMEOUT_SECONDS seconds." "$command"
      else
        handle_retry_error $exit_code "$output" "$command" $retry_count
      fi
      retry_count=$((retry_count + 1))
    fi
  done
  echo "[ERROR] All retries failed for command '$command'."
}
```
