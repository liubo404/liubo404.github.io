---
layout: post
title: "jQuery recipes"
description: ""
category: 
tags: [jquery]
---
{% include JB/setup %}

# Remove all HTML tags in a string with the jquery text() function

```javascript
$('div .news-info').each(function(){
	var v = $(this).text().replace(/(<([^>]+)>)/ig,"");
	$(this).html(v);
});
```
