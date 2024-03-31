#!/bin/bash

# change dir
cd ./projects/simple_shell

# Docker image name
IMAGE_NAME="simple_shell"

# Check if the Docker image exists
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo "Image does not exist. Building now..."
    docker build -t $IMAGE_NAME .
fi

cd -
gunicorn -b "127.0.0.1:5001"  api.v1.app:app
