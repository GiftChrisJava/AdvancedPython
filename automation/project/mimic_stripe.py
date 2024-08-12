#  write a function that mimics the strip()
# method, which removes leading and trailing 
# whitespace (or specified characters).
import re

def regex_strip(text, chars=None):
    if chars is None:
        # Default behavior: Remove whitespace
        return re.sub(r"^\s+|\s+$", "",text)
    else :
        # Create a regex pattern from the chars argument
        chars = re.escape(chars)  # Escape any special characters
        return re.sub(f"^[{chars}]+|[{chars}]+$", "", text)
    
    
# Test cases
print(regex_strip("  Hello, World!  "))      # Should return "Hello, World!"
print(regex_strip("xxHello, World!xx", 'x')) # Should return "Hello, World!"
print(regex_strip("***Hello***", '*'))       # Should return "Hello