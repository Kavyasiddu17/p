Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(0,17)
range(0, 17)
>>> list(range(0,17))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
>>> list(range(0,17,1))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
>>> list(range(0,17,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16]
>>> list(range(0,17,4))
[0, 4, 8, 12, 16]
>>> list(range(0,17,8))
[0, 8, 16]
>>> a=(2,8.7,'klm')
>>> a[1]
8.7
>>> a[1]=6.5
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[1]=6.5
TypeError: 'tuple' object does not support item assignment

>>> a=[2,8.7,'klm']
>>> a[1]=6.5
>>> a[1]
6.5
>>> b={2'8.7,'klm'}
SyntaxError: unterminated string literal (detected at line 1)
       
>>> b={2,8.7,'klm'}   
>>> print(b)   
{8.7, 2, 'klm'}
>>> b[2]=abc 
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b[2]=abc
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
       
>>> b[2]='abc'    
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b[2]='abc'
TypeError: 'set' object does not support item assignment
