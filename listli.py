Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=['kav',4.5,'girl',2,6,9]
b=[50,'mom',6.5,89,90]
c=[56,67,67,98,23,32,67]
k=[a,b]
print(k)
[['kav', 4.5, 'girl', 2, 6, 9], [50, 'mom', 6.5, 89, 90]]
a.append(5)
print(a)
['kav', 4.5, 'girl', 2, 6, 9, 5]
>>> b.insert(2,78)
>>> print(b)
[50, 'mom', 78, 6.5, 89, 90]
>>> c.remove(67)
>>> print(c)
[56, 67, 98, 23, 32, 67]
>>> a.pop(0)
'kav'
>>> print(a)
[4.5, 'girl', 2, 6, 9, 5]
>>> del a[3]
>>> print(a)
[4.5, 'girl', 2, 9, 5]
>>> a.extend('kav')
>>> print(a)
[4.5, 'girl', 2, 9, 5, 'k', 'a', 'v']
>>> occurence=c.count(67)
>>> print(c)
[56, 67, 98, 23, 32, 67]
>>> print(occurence)
2
>>> c=min(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c=min(a)
TypeError: '<' not supported between instances of 'str' and 'float'
>>> l=min(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l=min(a)
TypeError: '<' not supported between instances of 'str' and 'float'
>>> l=min(c)
>>> print(l)
23
>>> l=max(c)
>>> print(l)
98
>>> total=sum(c)
>>> print(total)
343
