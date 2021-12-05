def count_sheeps(sheep):
    return len([x for x in sheep if x])
    
"""def count_sheeps(sheep):
        return sheep.count(True)  """ 

lista = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
cuenta = count_sheeps(lista)    
print(cuenta)
      