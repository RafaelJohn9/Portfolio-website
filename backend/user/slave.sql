-- A SQL script  that is used to create a slave db and configuration of its files
CHANGE MASTER TO
  MASTER_HOST='external_mysql_host',
  MASTER_PORT=3306,
  MASTER_USER='replication_user',
  MASTER_PASSWORD='replication_password',
  MASTER_LOG_FILE='mysql-bin.00359',  -- Use SHOW MASTER STATUS on the master to get this value
  MASTER_LOG_POS=4757;                   -- Use SHOW MASTER STATUS on the master to get this value

START SLAVE;
SET GLOBAL read_only = OFF;
