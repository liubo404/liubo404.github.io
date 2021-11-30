---
layout: post
title: "java utils"
description: ""
category: 
tags: []
---
{% include JB/setup %}

```java
public class StringUtilities{
    public static Boolean isNumeric(String s){
        Boolean ReturnValue;
        try{
            Decimal.valueOf(s);
            ReturnValue = TRUE; 
        } catch (Exception e) {
            ReturnValue = FALSE;
        }
        return ReturnValue;
    }
}
//Sample runs:

list<String> slist = new list<String>{
  '12',       // TRUE
  '12.2',     // TRUE
  'string',   // FALSE
  '',         // FALSE
  NULL        // FALSE
};

for (String s : slist) system.debug(
    StringUtilities.isNumeric(s)
);

``` 
ref: [stackoverflow](https://salesforce.stackexchange.com/questions/165092/how-to-check-if-string-is-decimal)。

[baeldung](https://www.baeldung.com/java-check-string-number)