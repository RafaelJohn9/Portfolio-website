#!/bin/bash
# a scripts that installs the user_api

# Define variables
DOCKER_IMAGE="user_backend_api"
EXTERNAL_MYSQL_HOST="localhost"
EXTERNAL_MYSQL_USER="user"
MYSQL_ROOT_PASSWORD="password"
MYSQL_DATABASE="PortfolioDB"


# Connect container's MySQL db to the external MySQL
# docker run -it --rm -p 5000:5000 "$DOCKER_IMAGE" /bin/bash -c \
#	"service mariadb start && \
#	mysql -h'$EXTERNAL_MYSQL_HOST' \
#       -u'$EXTERNAL_MYSQL_USER' \
#       '$MYSQL_DATABASE'"

docker run -it --rm -p 5000:5000 "$DOCKER_IMAGE" /bin/bash -c \
  "service mariadb start && \
   mysql -h'$EXTERNAL_MYSQL_HOST' -u'root'\
        -e \"CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE;\" && \
   mysql -h'$EXTERNAL_MYSQL_HOST' -u'$EXTERNAL_MYSQL_USER' -p'$MYSQL_ROOT_PASSWORD' \
        -e \"CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE; \
        GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$EXTERNAL_MYSQL_USER'@'localhost' IDENTIFIED BY '$MYSQL_ROOT_PASSWORD';\" && \
   /usr/bin/cat models/engine/db.sql | mysql -u root
   source .api_keys.env && \
   exec /bin/bash"

