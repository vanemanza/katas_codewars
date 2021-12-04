def pig_it(text):
    #your code here
    lista = text.split(' ')
    nueva_lista = []
    for word in lista: 
        primera = word[0]    
        if word in ('¡!¿?'):
            nueva_palabra = word      
        elif len(word) == 1 :                       
            nueva_palabra = word + 'ay'    
        else:
            nueva_palabra = word[1:]+ primera +'ay' 
        nueva_lista.append(nueva_palabra)
    texto=' '.join(nueva_lista)
    return texto 

test1 = pig_it('Pig latin is cool')
test2 = pig_it('This is my string')    
test3 = pig_it('O tempora o mores !')

print(test1) 
print(test2) 
print(test3)

"""
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
"""