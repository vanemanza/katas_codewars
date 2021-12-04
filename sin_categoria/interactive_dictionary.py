"""
In this kata, your job is to create a class Dictionary which you can add
words to and their entries. Example:

>>> d = Dictionary()

>>> d.newentry('Apple', 'A fruit that grows on trees')

>>> print(d.look('Apple'))
A fruit that grows on trees

>>> print(d.look('Banana'))
Can't find entry for Banana
Good luck and happy coding!
"""

class Dictionary:
    def __init__(self):
        # Your code
        self.items_list = []
        
    def newentry(self, word, definition):
        # Your code
        self.item = (word, definition)
        self.items_list.append(self.item)              
        
    def look(self, key):        
            # your code        
        for item in self.items_list:
            if item[0] == key:
                return (item[1])
            
        return "Can\'t find entry for {}".format(key)  



d = Dictionary()
print(d)
    
d.newentry("Apple", "A fruit")
print(d.look("Apple")) #a fruit that grows on trees
print(d.items_list)   

d.newentry("Soccer", "A sport")
print(d.look("Soccer") ) # "A sport"
print(d.look("Hi")) # "Can't find entry for Hi"
print(d.look("Ball") ) # "Can't find entry for Ball"  
print(d.items_list)  

d.newentry("soccer", "a sport")
print(d.look("soccer") ) #"a sport"  
print(d.items_list)  
