"""
Given a string of digits confirm whether the sum of all the individual even 
digits are greater than the sum of all the indiviudal odd digits. 
Always a string of numbers will be given.

If the sum of even numbers is greater than the odd numbers return: 
"Even is greater than Odd"

If the sum of odd numbers is greater than the sum of even numbers return: 
"Odd is greater than Even"

If the total of both even and odd numbers are identical return: 
"Even and Odd are the same"

"""

def even_or_odd(s):    
    lista = []
    for x in s:
        lista.append(int(x))
    suma_pares = sum([x for x in lista if x%2==0])
    suma_impares = sum([x for x in lista if x%2!=0])
    if suma_pares == suma_impares:
        return "Even and Odd are the same"
    elif suma_pares > suma_impares:
        return  "Even is greater than Odd"  
    else:
        return  "Odd is greater than Even"   
 
test1 = even_or_odd('12')
test2 = even_or_odd('123')
test3 = even_or_odd('112')

print(test1)
print(test2)
print(test3) 

"""
def even_or_odd(s):    
    even_minus_odd = sum([-x if x % 2 else x for x in map(int, s)])
    if even_minus_odd > 0:
        return "Even is greater than Odd"
    elif even_minus_odd < 0:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
"""