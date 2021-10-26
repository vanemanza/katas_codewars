"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), 
value1(number), value2(number).
The function should return result of numbers after applying the chosen 
operation.
"""
def basic_op(operator, value1, value2):
    #your code here
    
    if operator is '/':
        if value1 == 0 or value2 == 0:
            return 'no se puede dividir por 0'
        return value1/value2    
    if operator is '+':
        return value1+value2
    if operator is '-':
        return value1-value2 
    if operator is '*':
        return value1*value2 

