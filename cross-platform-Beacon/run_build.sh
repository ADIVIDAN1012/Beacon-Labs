#!/bin/bash
set -e

# Ensure we are in the script's directory
cd "$(dirname "$0")"

# Add local bin to path
export PATH="$HOME/.local/bin:/usr/local/bin:$PATH"

echo "Starting Buildozer build at $(date)..." > build.log

# Run buildozer with auto-accept license config implied by spec
# Using 'exec' to replace shell with buildozer, avoiding process group issues
# Redirecting all output
buildozer android debug >> build.log 2>&1
