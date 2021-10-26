"""
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid
(2010) and After Earth (2013). Jaden is also known for some of his philosophy
that he delivers via Twitter. When writing on Twitter, he is known for almost
always capitalizing every word. For simplicity, you'll have to capitalize 
each word, check out how contractions are expected to be in the example 
below.

Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not capitalized 
in the same way he originally typed them.
"""

def to_jaden_case(string):
    lista = string.split()  
    nueva_palabra = ''
    nueva_lista = []
    for palabra in lista:
        nueva_palabra = palabra.capitalize()
        nueva_lista.append(nueva_palabra)
    nuevo_str = ' '.join(nueva_lista) 
    return nuevo_str

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))

#def toJadenCase(string):
  #  return ' '.join(x.capitalize() for x in string.split())