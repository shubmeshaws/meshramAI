```bash
function retry_command() {
  local command=$1
  local max_retries=$2

  # Input validation
  if [ -z "$command" ]; then
    echo "[ERROR] Command is required" >&2
    return 1
  fi
  if [ -z "$max_retries" ] || ! [[ $max_retries =~ ^[0-9]+$ ]] || [ $max_retries -le 0 ]; then
    echo "[ERROR] max_retries must be a positive integer" >&2
    return 1
  fi

  local retry_count=0
  local initial_sleep_time=1
  local sleep_time=$initial_sleep_time
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
      sleep $sleep_time
      sleep_time=$((sleep_time * 2))
      if [ $sleep_time -gt 30 ]; then
        sleep_time=30
      fi
    fi
  done
  echo "[ERROR] All retries failed for command '$command'."
}
```
