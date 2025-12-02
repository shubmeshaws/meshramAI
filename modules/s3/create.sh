```bash
#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -L "$SOURCE" ]; do
  DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$(cd -P "$(dirname "$SOURCE")/../.." >/dev/null 2>&1 && pwd)"

function s3_create() {
  BUCKET_NAME="$1"
  INPUT_REGION="$2"
  ACL="${3:-private}"

  if [[ -z "$BUCKET_NAME" || -z "$INPUT_REGION" ]]; then
    echo "[ERROR] Usage: meshram s3 create <bucket-name> <region> [public|private]"
    return 1
  fi

  REGION="$(awk -F= -v region="$INPUT_REGION" '$1 == region { print $2 }' "$SCRIPT_DIR/regions.conf")"
  REGION="${REGION:-$INPUT_REGION}"

  echo "[INFO] Creating bucket '$BUCKET_NAME' in region '$REGION' with ACL '$ACL'..."

  if [[ "$REGION" == "us-east-1" ]]; then
    if ! output=$(aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" --acl "$ACL" 2>&1); then
      echo "[ERROR] Failed to create bucket '$BUCKET_NAME' in region '$REGION':"
      echo "$output"
      return 1
    fi
  else
    if ! output=$(aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" --create-bucket-configuration LocationConstraint="$REGION" --acl "$ACL" 2>&1); then
      echo "[ERROR] Failed to create bucket '$BUCKET_NAME' in region '$REGION':"
      echo "$output"
      return 1
    fi
  fi

  echo "[SUCCESS] Bucket '$BUCKET_NAME' created in region '$REGION'."
}

# ✅ ACTUALLY CALL THE FUNCTION
s3_create "$@"
```
