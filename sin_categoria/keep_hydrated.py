"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres
 of water per hour of cycling.

You get given the time in hours and you need to return the number of litres 
Nathan will drink, rounded to the smallest value.
"""
import math
def litres(time):
    litros = (time*0.5)
    resultado = math.floor(litros)
    
    return resultado

test1 = litres(1)    
test2 = litres(1.5)   
test3 = litres(2)   

print(test1)
print(test2)
print(test3)