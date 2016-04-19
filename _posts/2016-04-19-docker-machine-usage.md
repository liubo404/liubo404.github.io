---
layout: post
title: "docker machine usage"
description: ""
category: 
tags: []
---
{% include JB/setup %}

# when use docker-machine on windows, when with some errors, use the following steps to solve the problem

## list docker machine
docker-machine ls


## start the default docker machine
docker-machine start default

## get the env from docker-machine
docker-machine env default --shell=cmd


## set evn in cmd line use the above output

SET DOCKER_TLS_VERIFY=1
SET DOCKER_HOST=tcp://192.168.99.100:2376
SET DOCKER_CERT_PATH=C:\Users\abc\.docker\machine\machines\default
SET DOCKER_MACHINE_NAME=default
REM Run this command to configure your shell:
REM     FOR /f "tokens=*" %i IN ('"C:\Program Files\Docker Toolbox\docker-machine.exe" env default --shell=cmd') DO %i


## after that, the cmd line can use docker properly.
docker ps -a
docker images


## build your own docker images
cd /workdock
ls
Dockerfile  README.md  empty  sources.list

docker build -t my-docker .

