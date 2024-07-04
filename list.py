Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> a=[1,6.5,pqr]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=[1,6.5,pqr]
NameError: name 'pqr' is not defined
>>> a=[1,6.5,'pqr']
>>> print(a)
[1, 6.5, 'pqr']
>>> a[2]
'pqr'
>>> a[-1]
'pqr'
>>> a[0]
1
>>> a[-2]
6.5
