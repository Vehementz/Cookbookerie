# Script that create 2 containers isolated in a specific custom network

#! /bin/bash
docker network create --driver=bridge --subnet="192.168.50.0/24" --gateway="192.168.50.254" web
docker network create --driver=bridge --subnet="192.168.51.0/24" --gateway="192.168.51.254" db
docker run -d --network db --name db mariadb -p 3306:3306 \ # Create a db container using the mariadb image
docker run -d --network web --name web nginx -p 8080:80 \ # Create a web container using the nginx image
docker network connect web db # Connect db container to web network
docker network connect db web # Connect web container to db network
