"""
You need to write a function that reverses the words in a given string.
A word can also fit an empty string. If this is not clear enough, here are 
some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary
 whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
"""

def reverse(st):
    # Your Code Here

    palabras = st.split(' ')
    palabras.sort(reverse=True)
    st = ' '.join(palabras)
    
    return st

test = reverse('Hello World')    
print(test)

"""
You have passed all of the tests! :)
"""