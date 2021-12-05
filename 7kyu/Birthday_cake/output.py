def cake(candles:int, debris:str) -> str:

    """
    Si la suma de debris > al 70% de candles, retorna Fire!
    Si no, retorna That was close!

    >>> cake(900, 'abcdef')
    'That was close!'

    >>> cake(56, 'ifkhchlhfd')  
    'Fire!'
    """
      
    def sumar(palabra):      
      puntos = []
      for x, y  in enumerate(palabra):
            
            posicion = x+1
            if posicion % 2 == 0:
                y = ord(y) - 96
                
            if posicion % 2 != 0:
                y = ord(y)  
            puntos.append(y)  
      return( sum(puntos))    

    if candles > 0:
                              
          setenta = candles*0.7
          puntos = sumar(debris)
          if puntos >= setenta:
              return 'Fire!'
          else:
              return 'That was close!'      
    else:
        return 'That was close!' 


#import string

#def cake(candles: int, debris: str) -> str:
 #   fallen_candles = sum(
  #      string.ascii_letters.index(char) if index % 2 else ord(char)
  #      for index, char in enumerate(debris)
   # )

    #return "Fire!" if candles and fallen_candles > candles * 0.7 else "That was close!"
  


      
      
            

  
      


  