Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=17
k=17
m=5
l=8.6
sum(a,b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sum(a,b)
NameError: name 'b' is not defined
sum(k,m)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sum(k,m)
TypeError: 'int' object is not iterable
sum(int('k','m'))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sum(int('k','m'))
TypeError: 'str' object cannot be interpreted as an integer
>>> print(k+m)
22
>>> print(k+l)
25.6
>>> print(k-m)
12
>>> sum(k+m)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sum(k+m)
TypeError: 'int' object is not iterable
>>> sum(int(k+m))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sum(int(k+m))
TypeError: 'int' object is not iterable
>>> print(k*m)
85
>>> print(k*l)
146.2
>>> print(k/l)
1.9767441860465118
>>> print(k/m)
3.4
>>> print(m/k)
0.29411764705882354
>>> print(k//m)
3
>>> print(k%m)
2
>>> print(k**m)
1419857
>>> mod(k,m)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    mod(k,m)
NameError: name 'mod' is not defined
