---
layout: post
title: "mysqldump duplication database copy paste"
description: ""
category: 
tags: []
---
{% include JB/setup %}


mysqldump -u root -ppassword tiantian | mysql -u root -ppassword tiantian_test;
