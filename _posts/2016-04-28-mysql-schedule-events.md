---
layout: post
title: "mysql schedule events"
description: ""
category: 
tags: [mysql]
---
{% include JB/setup %}

# Working with MySQL Scheduled Event
## How to Create Scheduled Events in MySQL


```sql
UPDATE t_card
SET is_pay = 1
WHERE
binduser_id IN (
SELECT
userid
FROM
t_alipayinfo
WHERE
tradestatus = 'TRADE_SUCCESS'
)
```

<img src="/img/mysql-events.png"/>
<img src="/img/mysql-events-2.png"/>
