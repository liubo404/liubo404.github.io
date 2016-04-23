---
layout: post
title: "mysqldump duplication database copy paste"
description: ""
category: 
tags: []
---
{% include JB/setup %}

```sql
mysqldump -u root -ppassword tiantian | mysql -u root -ppassword tiantian_test;
```



# add unique key to exists table

```sql
	ALTER TABLE t_seller ADD CONSTRAINT unq_username UNIQUE (username);
```

```sql
	ALTER TABLE t_seller ADD UNIQUE (usernem);
```


# modify timestamp column set default value
```sql
alter table t_voluntary_news MODIFY create_time timestamp default CURRENT_TIMESTAMP not null
```

# find duplicate rows

SELECT seq, COUNT(*) c FROM t_card GROUP BY seq HAVING c > 1;

# change id auto increament value
ALTER TABLE tablename AUTO_INCREMENT = 1000
