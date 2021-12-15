---
layout: post
title: "oracle row_number left join remove duplication"
description: ""
category: 
tags: []
---
{% include JB/setup %}

#  ora-00054:resource busy and acquire with NOWAIT specified  

```
select t2.username, t2.sid, t2.serial#, t2.logon_time
from v$locked_object t1,
     v$session t2
where t1.session_id = t2.sid
order by t2.logon_time;

ALTER SYSTEM KILL SESSION '2291,8603';
ALTER SYSTEM KILL SESSION 'SID,SERIAL#'; 

//others
select session_id from v$locked_object;
SELECT sid, serial#, username, osuser FROM v$session where sid = 142;
ALTER SYSTEM KILL SESSION '142,38';
```

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


ref:https://stackoverflow.com/questions/45480825/oracle-sql-duplicate-rows-when-joining-new-table

If joining another table into an existing query causes the existing rows to be duplicated, it is because the table being joined in has duplicate values in the columns that are being used as keys for the join

In your case, if you do

```
SELECT ENTITY_KEY FROM EVALUATE_RULE GROUP BY ENTITY_KEY HAVING COUNT(*) > 1
```

You'll see which entity_keys are duplicated. When these duplicates are joined to the existing data, the existing data has to be doubled up to permit both rows from EVALUATE_RULE with the same ENTITY_KEY to exist in the result set

You must either de-dupe the table, or put other clauses into your ON condition to further restrict the rows coming from EVALUATE_RULE.

For example, after adding EVALUATE_RULE and putting ER.* in your SELECT list, imagine that you can see that the rows from ER are status = 'old' and status = 'current' but you know you only want the current ones.. So put AND er.status = 'current' in your ON clause

Your comment indicates that multiple records differ by some column you don't care about, so this technique will just select only one row:

```
LEFT JOIN 
(SELECT e.*, ROW_NUMBER() OVER(PARTITION BY e.entity_key ORDER BY e.name) as rown FROM evaluate_rule e) er
ON
  er.entity_key = pr.account_key and 
  er.rown = 1
```

If you want info on why this works, run that sql in isolation:

```
SELECT e.*, ROW_NUMBER() OVER(PARTITION BY e.entity_key ORDER BY e.name) as rown FROM evaluate_rule e
```

ORDER BY e.entity_key -- i added this to make it more clear what is going on. You don't need it in your main query
It just assigns a number to each row in the table, the number restarts at 1 every time entity_key changes, so we can then select all those with rown = 1

If it turns out you DO want something specific like "the latest row from evaluate_rule", you can use something like this:

```
SELECT e.*, ROW_NUMBER() OVER(PARTITION BY e.entity_key ORDER BY e.created_date DESC) as rown FROM evaluate_rule e
```
Now the latest created_date row will always have rown = 1
 