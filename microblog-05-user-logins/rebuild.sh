#!/bin/bash
docker system prune
echo building docker container, this will generate a lot of output
docker-compose build
echo bringing up docker contain
docker-compose up

docker-compose down -v --rmi all --remove-orphans
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
docker volume rm $(docker volume ls -q)
