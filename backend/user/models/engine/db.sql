CREATE DATABASE PortfolioDB;

CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON PortfolioDB.* TO 'user'@'localhost';

FLUSH PRIVILEGES;