#!/bin/bash

# Docker image name
IMAGE_NAME="skills_backend_api"

# Check if the Docker image exists
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo "Image does not exist. Building now..."
    docker build -t $IMAGE_NAME .
fi

