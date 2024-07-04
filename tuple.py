Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuples
>>> (k,l,m)=([7,8],'ram',3.4)
>>> print(k)
[7, 8]
>>> print(m)
3.4
>>> print(l)
ram
>>> print(k,l,m)
[7, 8] ram 3.4
>>> j=(23,56,96,45,09,89,23,23)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> j=(23,56,96,90,89,23,23)
>>> a=j.count(11)
>>> print(a)
0
>>> a=j.count(23)
>>> print(a)
3
>>> h=j.index(56)
>>> print(h)
1
>>> s=max(j)
>>> print(s)
96
>>> q=min(j)
>>> print(q)
23
>>> first_item=j[1]
>>> print(first_item)
56
>>> 
>>> sample_tuple=(2,4,6,8)
>>> reversed_tuple=sample_tuple[::-2]
>>> print(f"original tuple:{sample_tuple}")
original tuple:(2, 4, 6, 8)
>>> print(f"reversed tuole:{sample_tuple}")
reversed tuole:(2, 4, 6, 8)
