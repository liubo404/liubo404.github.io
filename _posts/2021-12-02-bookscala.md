---
layout: post
title: "bookscala"
description: ""
category: 
tags: []
---
{% include JB/setup %}


## what is expression?
- the code can be evaluated and yield a value
- the code can be used inside large expression

```scala
(1 to 10).product //this is a expression

100 + (1 to 10).product + 100 //this another expression


// expression block
{ val n = 12345; n * n * n + n * n }

```

## predicate :  a function returns a booean value

## bound vs free
- bound variables 
  - variables that are defined only inside an expression 
  - invisible outside 
- free variables
  - variables used in an expression but defined outside it 
- bound vs free key difference
  - bound variables can be locally renamed at will

```scala
def isPrime(n: Int): Boolean = (2 to n - 1).forall(k => n % k != 0)
// n is free variable
// k is bound variable
// k can locally renamed to z
```

### transformation
transformation is a function taking a list of values and returning another list of values
```scala
List(1, 2, 3, 4, 5).filter(k => k % 3 != 0)
List(1, 2, 3).map { x => x * 2 }
```

### aggregation
aggregation is a function taking a list of values and returing a single value
```scala
List(10, 20, 30).max
List(10, 20, 30).sum
```

### map/reduce style
writing programs by chaining together various methods of transformation and aggregation is know as programming in the map/reduce style.

