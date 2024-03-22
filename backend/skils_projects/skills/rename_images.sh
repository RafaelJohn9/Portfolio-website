#!/bin/bash

# Define the directory to search
dir="./images"

# Use find to go through the directory recursively
find "$dir" -type f -name "*.svg" | while read -r file
do
    # Extract the directory name and the base name of the file
    dir_name=$(dirname "$file")
    base_name=$(basename "$file")

    # Use sed to remove 'icons8-' from the base name
    new_base_name=$(echo "$base_name" | sed 's/icons8-//')

    # Rename the file
    mv "$file" "$dir_name/$new_base_name"
done