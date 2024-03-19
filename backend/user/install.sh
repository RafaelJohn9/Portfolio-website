#!/bin/bash
# a scripts that installs the user_api

# Define variables
DOCKER_IMAGE="user_backend_api"
EXTERNAL_MYSQL_HOST="127.0.0.1"
EXTERNAL_MYSQL_USER="user"
MYSQL_ROOT_PASSWORD="password"
MYSQL_DATABASE="PortfolioDB"

cat models/engine/db.sql | sudo mysql -u root

# Connect container's MySQL db to the external MySQL
docker run -it --rm -p 5000:5000 "$DOCKER_IMAGE" /bin/bash -c \
  "service mariadb start && 
  cat models/engine/db.sql | mysql -uroot &&\
  cat slave.sql | mysql -uroot &&\

   mysql -h'$EXTERNAL_MYSQL_HOST' -u'$EXTERNAL_MYSQL_USER' -p'$MYSQL_ROOT_PASSWORD' \
        -e \"USE $MYSQL_DATABASE;\" && \

   source .api_keys.env && \
   exec /bin/bash"
