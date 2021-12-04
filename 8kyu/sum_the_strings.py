"""
Create a function that takes 2 integers in form of a string as an input, and outputs the sum 
(also as a string):
"""

def sum_str(a, b):
    suma = int(a) + int(b)
    if a == '':
        a='0'
    if b == '':
        b = '0'
    return str(suma)

a = (input('ingresa un numero  '))
b = (input('ingresa otro numero  '))   
test = sum_str(a, b)   
print(test)