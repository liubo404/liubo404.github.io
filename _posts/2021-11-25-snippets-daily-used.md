---
layout: post
title: "snippets daily used"
description: ""
category: 
tags: []
---
{% include JB/setup %}

# shell

```bash
# 1. copy file from remote server to current directory  
cd /tmp
scp user_name@xxx.xxx.xxx.xxx:/path/to/file .
# then input the password of user_name
# .dot means current directory


# 2.show wifi password
$ sudo grep psk= /etc/NetworkManager/system-connections/*

cd /etc/NetworkManager/system-connections/
ls -a
sudo cat [name of profile]


```