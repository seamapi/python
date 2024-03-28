#!/usr/bin/env bash
set -e # Exit immediately if a command exits with a non-zero status.

# Save the current script directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Define the path of a temporary directory for storing the generated SDK code
TEMP_DIR="$SCRIPT_DIR/temp_sdk"

# Create the temporary directory
mkdir -p $TEMP_DIR

cd ..

# Run the SDK generator command
nextlove-sdk-generator generate python $TEMP_DIR

cd "$SCRIPT_DIR"

# Check if the temp directory was created successfully
if [ ! -d "$TEMP_DIR" ]; then
    echo "Failed to generate SDK"
    exit 1
fi

rm -rf ../seamapi
mv $TEMP_DIR/seamapi ../seamapi

# Copy any other files that don't exist in the root directory
for file in $TEMP_DIR/*; do
    if [ ! -e "../$(basename "$file")" ]; then
        mv "$file" ..
    fi
done

# Remove the temporary directory
rm -rf $TEMP_DIR

echo "SDK generation complete."
