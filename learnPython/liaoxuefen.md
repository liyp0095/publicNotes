# liaoxuefeng python

https://www.liaoxuefeng.com/wiki/1016959663602400/1017316949097888

```python
sorted(dict.items(), lambda x:x[2], reverse=True)
```

## diedai

```python
data = [1,2,3,4]
for i in range(len(data)):
  print(i)

for c in "ABC":
  print(c)

>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False

for i, value in enumerate(['A', 'B', 'C']):
  print(i, value)
```

- dict.items()
-

## List Comprehensions

```python
data = [x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]

# 还可以使用两层循环，可以生成全排列：
[m + n for m in 'ABC' for n in 'XYZ']

[d for d in os.listdir('.')] # os.listdir可以列出文件和目录

import os
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
```

## generator

two method
- with ()
- with yield

```python
g = (x * x for x in range(10))
# g is generator
next(g)
# last next(g) cause error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

# 基本上永远不会调用next() 而是通过for循环来迭代它，并且不需要关心StopIteration的错误

for n in g:
  print(n)

# fibonacci
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```
