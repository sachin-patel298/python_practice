Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

car = "BMW"
first_char = car[0]
print(first_char)
B
chai = "Masala Chai"
slice_chai = chai[0:9]
print(slice_chai)
Masala Ch
slice_chai = chai[0:9]
slice_chai = chai[0:6]
print(slice_chai)
Masala
num_list = "0123456789"
num_list[:]
'0123456789'
num_list[2:]
'23456789'
num_list[:3]
'012'
num_list[0:9:3]
'036'
num_list[-1:5]
''
chai
'Masala Chai'
print(chai.lower())
masala chai
print(chai.upper())
MASALA CHAI
chai
'Masala Chai'
chai = "  Masala  "
print(chai.strip())
Masala
print(chai.replace("Masala,Tadka"))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(chai.replace("Masala,Tadka"))
TypeError: replace expected at least 2 arguments, got 1
print(chai.replace("Masala","Tadka"))
  Tadka  
print(chai)
  Masala  
chai = "Lemon , Ginger , Masala , Mint"
print(chai.split(", "))
['Lemon ', 'Ginger ', 'Masala ', 'Mint']
print(chai.find("Masala"))
17
 chai = "Masala Chai Chai Chai"
 
SyntaxError: unexpected indent
chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))
3
chai_type = "Masala"
quantity = 2
order = "I ordered {} Cups of {} Chai"
order
'I ordered {} Cups of {} Chai'
print(chai.format(quantity,chai_type))
Masala Chai Chai Chai
>>> print(order.format(quantity,chai_type))
I ordered 2 Cups of Masala Chai
>>> chai = ["Lemon" , "Ginger" , "Masala" , "Mint"]
>>> print(" ".join(chai))
Lemon Ginger Masala Mint
>>> print(", ".join(chai))
Lemon, Ginger, Masala, Mint
>>> print("=".join(chai))
Lemon=Ginger=Masala=Mint
>>> chai = "Masala chai"
>>> print(len(chai))
11
>>> for letter in chai:
...     print(letter)
... 
...     
M
a
s
a
l
a
 
c
h
a
i
>>> chai = "He said , \"Masal Chai is Awesome\""
>>> chai
'He said , "Masal Chai is Awesome"'
>>> chai = r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
>>> chai = "Masala Chai"
>>> print("Masala" in chai)
True
