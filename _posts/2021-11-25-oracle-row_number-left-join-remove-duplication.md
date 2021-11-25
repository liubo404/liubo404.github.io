---
layout: post
title: "oracle row_number left join remove duplication"
description: ""
category: 
tags: []
---
{% include JB/setup %}

# row_number() over(partition by order by )使用说明书
## 作用：数据库去除重复记录，进行排序。

```
语法：ROW_NUMBER() OVER (PARTITION BY COL1 ORDER BY COL2)
功能：表示根据COL1分组，在分组内部根据 COL2排序，而这个值就表示每组内部排序后的顺序编号（组内连续的唯一的）
row_number() 返回的主要是“行”的信息，并没有排名 

--在test表中根据name分组，age进行排序
select name,age,row_number() over(partition by name order by
age desc) from test;

--去掉重复的记录
select * from (select name,age,row_number() over( partition by name 
order by age desc) rn from test )where rn= 1;



SELECT f.id,
       f.name,
       f.FORM_STATUS,
       f.TYPE as formType,
       d.PROCESS_NAME,
       d.status,
       d.id   as processId,
       d.LAST_MODIFY_USER_ID,
       d.LAST_MODIFY_TIME
FROM TBL_FORM_MODEL f
         LEFT JOIN
     (select b.*,  row_number() over ( partition by b.id  order by b.id desc ) rn_
      from TBL_FORM_MODEL a,
           TBL_PROCESS_DEFINITION b
      WHERE a.id = b.FORM_ID
        and b.STATUS = 1
        and b.DELETED = 0
      order by b.id desc) d
     on d.FORM_ID = f.ID   and d.rn_ =1
WHERE f.DELETED = 0
order by f.id;
```