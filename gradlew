#!/bin/bash
# This is a simplified gradlew script for demonstration purposes
# In a real environment, this would be a proper wrapper script

echo "This is a placeholder gradlew script"
echo "In GitHub Actions, the gradle command will be available directly"

# Determine the command to run
GRADLE_CMD="$1"

# Process any additional arguments
for arg in "${@:2}"; do
    GRADLE_CMD="$GRADLE_CMD $arg"
done

# Execute the gradle command directly (GitHub Actions has gradle installed)
if command -v gradle &> /dev/null; then
    exec gradle $GRADLE_CMD
else
    echo "Error: gradle command not found"
    exit 1
fi