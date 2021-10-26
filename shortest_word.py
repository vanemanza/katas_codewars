"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data 
types.
"""

def find_short(s):
    # your code here
    words = s.split(' ')
    shortest = words[0]
    l = len(shortest)
    for word in words:
        
        if len(word)<len(shortest):
            shortest = word 
            l = len(shortest)
            
    return l

    #def find_short(s):
     #   return min(len(x) for x in s.split())

test1 = find_short('bitcoin take over the world maybe who knows perhaps')    
print(test1)
test2 = find_short('i want to travel the world writing code one day')
print(test2)