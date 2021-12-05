"""
It's your birthday. Your colleagues buy you a cake. The numbers of candles on the cake is provided (candles). Please note this is not reality, and your age can be anywhere up to 1000. Yes, you would look a mess.

As a surprise, your colleagues have arranged for your friend to hide inside the cake and burst out. They pretend this is for your benefit, but likely it is just because they want to see you fall over covered in cake. Sounds fun!

When your friend jumps out of the cake, he/she will knock some of the candles to the floor. If the number of candles that fall is higher than 70% of total candles, the carpet will catch fire.

You will work out the number of candles that will fall from the provided lowercase string (debris). You must add up the character ASCII code of each even indexed (assume a 0 based indexing) character in the string, with the alphabetical position ("a" = 1, "b" = 2, etc.) of each odd indexed character to get the string's total.

For example:

"abc"  -->  "a" = 97, "b" = 2, "c" = 99  -->  total = 198
If the carpet catches fire, return "Fire!", if not, return "That was close!".

Notes

if there are no candles to begin with, the carpet cannot catch fire;
as this is not reality, you may have more candles falling from the cake than the total...
"""

         
      
def cake(candles,debris):
      
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


test1 = cake(900, 'abcdef')      
test2 = cake(56, 'ifkhchlhfd')  
test3 = cake(256, 'aaaaaddddr')
test4 = cake(333, 'jfmgklfhglbe')
test5 = cake(0, 'jaam')

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)

"""
import string


def cake(candles: int, debris: str) -> str:
    fallen_candles = sum(
        string.ascii_letters.index(char) if index % 2 else ord(char)
        for index, char in enumerate(debris)
    )

    return "Fire!" if candles and fallen_candles > candles * 0.7 else "That was close!"
"""      


      
      
            

  
      


  