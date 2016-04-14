---
layout: post
title: "jquery trim all white space when input finished"
description: ""
category: 
tags: []
---
{% include JB/setup %}
The example below removes all spaces from the contents of the textbox on focus. This particular example requires jQuery 1.7+ since it uses the new .on() API:

```javascript
$(function() {
	$("#dest").on("focus", function() {
		var dest = $(this);
		dest.val(dest.val().split(" ").join(""));
	});
});
```


This function is working fine for your scenario. As it is taking only one space between character and not allow more than 2 space


```javascript
$(function() {
	$("#dest").on("focusout", function() {
		var dest = $(this);
		dest.val(jQuery.trim(dest.val()));
		dest.val(dest.val().replace(/[ ]{2,}/, ' '));
	});
});
```
