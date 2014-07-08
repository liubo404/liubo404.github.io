---
layout: post
title: "Integer vs int"
description: ""
category: 
tags: []
---
{% include JB/setup %}
##Java Integer vs. int
<code>
public class inttest {
    public static void main(String[] args) {
        Integer i = 100;
        Integer j = 100;
        System.out.println(i == j);

        Integer x = 200;
        Integer y = 200;
        System.out.println(x == y);

        System.out.println(x+y);
    }
}

</code>
<img src='/img/java_int.png'/>
