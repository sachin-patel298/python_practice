Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tea_types = ("Black", "Green" ,"Oolong")
tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1:]
('Green', 'Oolong')
>>> len(tea_types)
3
>>> more_tea = ("Herbal","Earl Grey")
>>> all_tea = more_tea + tea_types
>>> print(all_tea)
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Black" in tea_types :
...     print("Black Is Available")
... else :
...     print("Not")
... 
...     
Black Is Available
>>> more_tea = ("Herbal","Earl Grey", "Herbal")
>>> more_tea.count("Herbal")
2
>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black,green,Oolong) = tea_types
>>> green
'Green'
>>> type(tea_type)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    type(tea_type)
NameError: name 'tea_type' is not defined. Did you mean: 'tea_types'?
>>> type(tea_types)
<class 'tuple'>
