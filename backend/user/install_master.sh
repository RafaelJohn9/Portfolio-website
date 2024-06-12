#!/bin/bash
# a scripts that installs the user_api

# Define variables
DOCKER_IMAGE="user_backend_api"
EXTERNAL_MYSQL_HOST="127.0.0.1"
EXTERNAL_MYSQL_USER="user"
MYSQL_ROOT_PASSWORD="password"
MYSQL_DATABASE="PortfolioDB"

# Check if the Docker image exists
if [[ "$(docker images -q $DOCKER_IMAGE 2> /dev/null)" == "" ]]; then
     # Docker image does not exist, so build it
     docker build -t "$DOCKER_IMAGE" .
else
     echo "Docker image $DOCKER_IMAGE already exists. Continuing run..."
fi


# Check if the docker volume exists
if [ $(docker volume ls -q -f name=mariadb_data) ]; then
     echo "Volume mariadb_data already exists."
else
     # Build the docker volume
     docker volume create mariadb_data
fi

# Connect container's MySQL db to the external MySQL
docker run -d  --env-file ~/Portfolio-website/backend/user/.api_keys.env -t -p 5000:5000 -v mariadb_data:/var/lib/mysql -v ${PWD}:/app "$DOCKER_IMAGE" /bin/bash -c \
     "service mariadb start && 
     cat models/engine/db.sql | mysql -uroot &&\
     source .api_keys.env  && \
     python3 ./run.py"
