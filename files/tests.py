# creating folders
import os

# os.makedirs("C:/Users/Gift Chris/Desktop/AdvancedPy/files/created")

print(os.path.abspath("."))
print(os.path.abspath(".\\Scripts"))
print(os.path.isabs("C:/Users/Gift Chris/Desktop/AdvancedPy/files/created"))
print(os.path.isabs("."))

# list of filename string for each file 
print(len(os.listdir("C:/Users/Gift Chris/Desktop")))


# finding total number files storage
totalSize = 0
for filename in os.listdir("C:/Users/Gift Chris/Desktop"):
    filenameSize = os.path.getsize(os.path.join("C:/Users/Gift Chris/Desktop", filename))
    
    totalSize = totalSize + filenameSize
    
print(totalSize / 1000, "mbs")