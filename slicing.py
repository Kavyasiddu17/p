Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##slicing and indexing
>>> k={completing python course}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> k={'completing python course'}
>>> print('k')
k
>>> print(k)
{'completing python course'}
>>> len(k)
1
>>> print(len(k))
1
>>> print(len('k'))
1
>>> a='completing python course'
>>> print(len(a))
24
>>> print k[0:7]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> a='computer science'
>>> print a[0:4]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(a[0:4])
comp
>>> print(k[0:7])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(k[0:7])
TypeError: 'set' object is not subscriptable
