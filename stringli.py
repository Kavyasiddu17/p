Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> k="   june month is a rainy month    "
>>> k.upper()
'   JUNE MONTH IS A RAINY MONTH    '
>>> k.lower()
'   june month is a rainy month    '
>>> k.startswith('june')
False
>>> k.endswith('month')
False
>>> k.replace('is','was')
'   june month was a rainy month    '
>>> x.lstrip()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x.lstrip()
NameError: name 'x' is not defined
>>> k.lstrip()
'june month is a rainy month    '
>>> k.rstrip()
'   june month is a rainy month'
>>> k.find('month')
8
