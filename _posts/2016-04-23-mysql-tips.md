---
layout: post
title: "mysql tips"
description: ""
category: 
tags: [mysql]
---
{% include JB/setup %}

# table CRUD

## add index
```sql
ALTER TABLE table_name ADD INDEX (column_to_index);
```













## generate random number between 1 and 100
```sql
	UPDATE t_course_wk SET course_wk_id =  FLOOR(RAND() * (100 + 1)) +1
```
