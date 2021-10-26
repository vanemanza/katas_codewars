"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

def reverse_words(text):

    lista = text.split() 
    nuevo_texto = []
    for palabra in lista:
        reverse = ''
        for letra in palabra:
            reverse = letra + reverse
        nuevo_texto.append(reverse)
    str = ' '.join(nuevo_texto)    
    return str
 
        
test1 = reverse_words('The quick brown fox jumps over the lazy dog.')      
print(test1)  
test2 = reverse_words('apple')      
print(test2)  
test3 = reverse_words('a b c d')      
print(test3)  
test4 = reverse_words('double  spaced  words')      
print(test4)  