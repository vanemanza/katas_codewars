"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything 
 exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""

#def validate_pin(pin):
    #return true or false
 #   if pin.isdigit():
  #      if len(pin)==4 or len(pin)==6 :
   #         return True
    #return False

validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()    