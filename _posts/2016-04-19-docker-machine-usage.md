---
layout: post
title: "docker machine usage"
description: ""
category: 
tags: [docker]
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
```
SET DOCKER_TLS_VERIFY=1
SET DOCKER_HOST=tcp://192.168.99.100:2376
SET DOCKER_CERT_PATH=C:\Users\abc\.docker\machine\machines\default
SET DOCKER_MACHINE_NAME=default
REM Run this command to configure your shell:
REM     FOR /f "tokens=*" %i IN ('"C:\Program Files\Docker Toolbox\docker-machine.exe" env default --shell=cmd') DO %i
```

## after that, the cmd line can use docker properly.
docker ps -a
docker images


## build your own docker images
```
cd /workdock
ls
Dockerfile  README.md  empty  sources.list

docker build -t my-docker .
```


### use putty instead of cmd connect to docker machine
Login with PUTTY instead of using the CMD
Docker Machine generates and uses the public/private key pair in your %USERPROFILE%\.docker\machine\machines\<name_of_your_machine> directory. To log in you need to use the private key from this same directory. The private key needs to be converted into the format PuTTY uses. You can do this with puttygen:

Open puttygen.exe and load (“File”->“Load” menu) the private key from (you may need to change to the All Files (*.*) filter)

%USERPROFILE%\.docker\machine\machines\<name_of_your_machine>\id_rsa
Click “Save Private Key”.

Use the saved file to login with PuTTY using docker@127.0.0.1:2022


<img src="/img/dm-docker.png"/>
