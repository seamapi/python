#!/bin/bash
set -e # Exit immediately if any command exits with a non-zero status.

mkdir -p ./tmp

# Remove the existing temporary SDK generation folder
rm -rf ./tmp/nextlove-sdk-generator-output

# Generate SDK files
nextlove-sdk-generator generate python ./tmp/nextlove-sdk-generator-output

# Move only the 'seam' folder
rm -rf ./seam
mv ./tmp/nextlove-sdk-generator-output/seam ./seam

# Clean up the temporary SDK generation folder
rm -rf ./tmp/nextlove-sdk-generator-output
