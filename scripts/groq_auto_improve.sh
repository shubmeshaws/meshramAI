#!/bin/bash

# Daily Code Improvement Script using Groq API (FREE!)
# This script analyzes code files and makes AI-powered improvements

# Configuration
GROQ_API_KEY="$GROQ_API_KEY"
MODEL="llama-3.3-70b-versatile"  # Best free model on Groq
MAX_TOKENS=4000

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if API key is set
if [[ -z "$GROQ_API_KEY" ]]; then
    echo -e "${RED}Error: GROQ_API_KEY environment variable is not set${NC}"
    echo "Please set your API key:"
    echo "  export GROQ_API_KEY='your-api-key-here'"
    echo ""
    echo "Get your FREE API key from: https://console.groq.com/"
    echo "No credit card required!"
    exit 1
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}Error: Not a git repository${NC}"
    exit 1
fi

# Function to call Groq API
call_groq() {
    local prompt="$1"
    local system_message="$2"

    # Use Python to properly escape JSON
    local json_payload=$(python3 << EOF
import json
import sys

prompt = """$prompt"""
system_message = """$system_message"""

payload = {
    "model": "$MODEL",
    "messages": [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ],
    "max_tokens": $MAX_TOKENS,
    "temperature": 0.7
}

print(json.dumps(payload))
EOF
)

    response=$(curl -s https://api.groq.com/openai/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $GROQ_API_KEY" \
        -d "$json_payload")

    echo "$response"
}

# Function to extract content from Groq response
extract_content() {
    local response="$1"
    echo "$response" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data['choices'][0]['message']['content'])
except:
    print('')
"
}

# Function to get improvement suggestion
get_improvement_suggestion() {
    local file_content="$1"
    local filename="$2"

    local system_msg="You are an expert code reviewer and software engineer. Analyze code and suggest ONE specific, practical improvement. Focus on: code quality, performance, readability, best practices, or adding useful features. Be concise and actionable."

    local prompt="Analyze this file ($filename) and suggest ONE specific improvement. Provide your response in this EXACT format:

DESCRIPTION: [Brief 1-2 sentence description of the improvement]
COMMIT_MESSAGE: [Format: 'type: description' e.g., 'refactor: improve error handling']
IMPROVED_CODE:
[Complete improved code here]

Current file content:
\`\`\`
$file_content
\`\`\`"

    call_groq "$prompt" "$system_msg"
}

# Function to select a random file to improve
select_file_to_improve() {
    # Get list of code files (exclude common non-code files)
    files=$(git ls-files | grep -E '\.(py|js|ts|jsx|tsx|java|cpp|c|go|rs|rb|php|swift|kt|sh)$' | grep -v -E '(node_modules|venv|__pycache__|\.git|dist|build)')

    if [[ -z "$files" ]]; then
        echo ""
        return
    fi

    # Select random file
    file=$(echo "$files" | shuf -n 1)
    echo "$file"
}

# Function to create new feature file
create_new_feature() {
    local system_msg="You are an expert software engineer. Create a new, useful utility function or module that would be valuable for this project."

    local existing_files=$(git ls-files | head -20)

    local prompt="Based on this project structure, create ONE new useful utility file.

Project files:
$existing_files

Provide your response in this EXACT format:
FILENAME: [e.g., utils/helper.py]
DESCRIPTION: [Brief description]
COMMIT_MESSAGE: [Format: 'type: description']
CODE:
[Complete code content]"

    call_groq "$prompt" "$system_msg"
}

# Main improvement logic
main() {
    echo -e "${BLUE}=== Daily Code Improvement (Groq AI - FREE!) ===${NC}"
    echo "Repository: $(pwd)"
    echo "Date: $(date)"
    echo ""

    # Decide: improve existing file (70%) or create new feature (30%)
    action=$((RANDOM % 100))

    if [[ $action -lt 70 ]]; then
        # Improve existing file
        echo -e "${YELLOW}Selecting file to improve...${NC}"
        file=$(select_file_to_improve)

        if [[ -z "$file" ]]; then
            echo -e "${RED}No code files found to improve${NC}"
            exit 1
        fi

        echo -e "${GREEN}Selected: $file${NC}"
        echo ""

        # Read file content
        file_content=$(cat "$file")

        if [[ ${#file_content} -gt 8000 ]]; then
            echo -e "${YELLOW}File too large, using first 8000 chars${NC}"
            file_content=$(echo "$file_content" | head -c 8000)
        fi

        echo -e "${YELLOW}Analyzing code with Groq AI...${NC}"
        response=$(get_improvement_suggestion "$file_content" "$file")

        # Extract content
        content=$(extract_content "$response")

        if [[ -z "$content" ]]; then
            echo -e "${RED}Failed to get response from Groq${NC}"
            echo "Response: $response"
            exit 1
        fi

        # Parse response
        description=$(echo "$content" | grep "DESCRIPTION:" | sed 's/DESCRIPTION: //' | head -1)
        commit_msg=$(echo "$content" | grep "COMMIT_MESSAGE:" | sed 's/COMMIT_MESSAGE: //' | head -1)

        # Extract improved code (everything after IMPROVED_CODE:)
        improved_code=$(echo "$content" | awk '/IMPROVED_CODE:/,0' | tail -n +2)

        if [[ -z "$improved_code" ]] || [[ -z "$commit_msg" ]]; then
            echo -e "${RED}Failed to parse valid improvement from Groq${NC}"
            echo "Content: $content"
            exit 1
        fi

        echo -e "${GREEN}Improvement: $description${NC}"
        echo -e "${GREEN}Commit: $commit_msg${NC}"
        echo ""

        # Apply improvement
        echo "$improved_code" > "$file"

        # Commit changes
        git add "$file"
        git commit -m "$commit_msg"

        echo -e "${GREEN}✓ Successfully improved $file${NC}"

    else
        # Create new feature
        echo -e "${YELLOW}Creating new feature file...${NC}"
        response=$(create_new_feature)

        content=$(extract_content "$response")

        if [[ -z "$content" ]]; then
            echo -e "${RED}Failed to get response from Groq${NC}"
            exit 1
        fi

        # Parse response
        filename=$(echo "$content" | grep "FILENAME:" | sed 's/FILENAME: //' | head -1)
        description=$(echo "$content" | grep "DESCRIPTION:" | sed 's/DESCRIPTION: //' | head -1)
        commit_msg=$(echo "$content" | grep "COMMIT_MESSAGE:" | sed 's/COMMIT_MESSAGE: //' | head -1)
        code=$(echo "$content" | awk '/CODE:/,0' | tail -n +2)

        if [[ -z "$filename" ]] || [[ -z "$code" ]]; then
            echo -e "${RED}Failed to generate new feature${NC}"
            echo "Content: $content"
            exit 1
        fi

        # Create directory if needed
        mkdir -p "$(dirname "$filename")"

        # Write file
        echo "$code" > "$filename"

        echo -e "${GREEN}Created: $filename${NC}"
        echo -e "${GREEN}Description: $description${NC}"
        echo ""

        # Commit
        git add "$filename"
        git commit -m "$commit_msg"

        echo -e "${GREEN}✓ Successfully created $filename${NC}"
    fi

    echo ""
    echo -e "${BLUE}Latest commits:${NC}"
    git log --oneline -5

    echo ""
    echo -e "${GREEN}Done! Push changes with: git push origin main${NC}"
}

# Run main function
main
