#!/bin/bash

# Function to recursively search for __pycache__ directories and add them to .gitignore
function add_to_gitignore {
    local dir="$1"
    local gitignore_file="$dir/.gitignore"

    # Check if __pycache__ directory exists in the current directory
    if [ -d "$dir/__pycache__" ]; then
        # Add __pycache__ to .gitignore if not already present
        if ! grep -q "__pycache__" "$gitignore_file"; then
            echo "__pycache__" >> "$gitignore_file"
            echo "Added __pycache__ to $gitignore_file"
        fi
    fi

    # Recursively search subdirectories
    for subdir in "$dir"/*; do
        if [ -d "$subdir" ]; then
            add_to_gitignore "$subdir"
        fi
    done
}

# Directory to start searching (change this to the desired directory)
start_directory="."

# Check if the start directory exists
if [ -d "$start_directory" ]; then
    add_to_gitignore "$start_directory"
    echo "Search complete."
else
    echo "Directory '$start_directory' not found."
fi
