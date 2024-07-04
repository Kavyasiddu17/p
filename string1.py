Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
k='basic modeling'
print(k)
basic modeling
len(k)
14
k[2:5:-1]
''
>>> k[5:3:-5]
' '
>>> k[5:3:-3]
' '
>>> k.upper()
'BASIC MODELING'
>>> k.lower()
'basic modeling'
>>> fruit="apple"
>>> m.fruit.replace('apple','mango')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    m.fruit.replace('apple','mango')
NameError: name 'm' is not defined
>>> print(m)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(m)
NameError: name 'm' is not defined
>>> m=fruit.replace('apple','mango')
>>> print(m)
mango
>>> name='  custerd   '
>>> name.lstrip()
'custerd   '
>>> name.rstrip()
'  custerd'
>>> text='welcome to Besant'
>>> index=text.find('sant')
>>> print(index)
13
>>> result=text.endswith('to')
>>> print(result)
False
>>> result=text.endswith('ant')
>>> print(result)
True
>>> result=text.startswith('wel')
>>> print(result)
True
