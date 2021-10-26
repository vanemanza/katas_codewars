"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string 
of those numbers in the form of a phone number.
"""

def create_phone_number(n):
    #your code here
    cadena = ''.join([str(x) for x in n])    
    return f'({cadena[0:3]}) {cadena[3:6]}-{cadena[6:]}'
    
test = create_phone_number([3,5,1,2,6,8,2,2,3,3])    
print(test)

"""
respuestas de Codewars

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])    

"""