Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> k=17
>>> m=5
>>> id(k)
140734226766776
>>> id(m)
140734226766392
>>> id(k)==id(m)
False
>>> a=17
>>> id(a)
140734226766776
>>> a=16
>>> id(a)
140734226766744
>>> b=16
>>> id(b)
140734226766744
>>> print('py value')
py value
>>> print('pi value')
pi value
>>> pi=22/7
>>> print(pi)
3.142857142857143
