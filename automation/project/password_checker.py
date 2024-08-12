# Strong password should have 
#     at least 8 charecters long 
#     contains both uppercase and lowercase chars 
#     have at least one digit

import re

def is_strong_password(password):
    #check password length
    if len(password) < 8:
        return False
    
    # check for uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # check for lower letter
    if not re.search(r'[a-z]', password):
        return False
    
    # check for digit
    if not re.search(r'\d+', password):
        return False
    
    return True

# Test cases
print(is_strong_password("Password1"))  # Should return True
print(is_strong_password("weakpass"))     # Should return False
print(is_strong_password("Short1"))       # Should return False
print(is_strong_password("NoDigitsHere")) # Should return False