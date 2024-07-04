Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=2
x
2
id(x)
140734165490136
p(id(x))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    p(id(x))
NameError: name 'p' is not defined
print(id(x))
140734165490136

x=4
y=5
id(x)
140734165490200
id(y)
140734165490232
x+y
9
z=x+y
z
9
>>> id(z)
140734165490360
>>> 140734165490360
140734165490360
>>> a=10
>>> b=a
>>> b
10
>>> id(b)
140734165490392
>>> id(a)
140734165490392
>>> 140734165490392
140734165490392
>>> id(a)==id(b)
True
>>> True
True
>>> 
>>> <class "float">
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> 
>>> type(a)
<class 'int'>
>>> b=none
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> b=None
>>> type(b)
<class 'NoneType'>
>>> <class 'NoneType'>
SyntaxError: invalid syntax
>>> a='546'
>>> int(a)=
SyntaxError: cannot assign to function call
>>> 
>>> 
