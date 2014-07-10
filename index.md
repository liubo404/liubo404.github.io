---
layout: page
title: liubo404's Home Page
---
{% include JB/setup %}


    Resume
    Programmer...want to be a CodeGuru...too hard to be...


##My Posts
<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>





