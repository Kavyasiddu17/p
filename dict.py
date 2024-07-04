Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #lists
>>> keys=['name','class','city']
>>> values=['kav',5,'blg']
>>> #dictionary useing zip
>>> sample_dict=dict(zip(keys,values))
>>> print(sample_dict)
{'name': 'kav', 'class': 5, 'city': 'blg'}
>>> #get()
>>> 
>>> class=sample_dict.get('class')
SyntaxError: invalid syntax
>>> print(f"Class:{class}")
SyntaxError: f-string: expecting a valid expression after '{'
