# This program reads a text file and replaces 
# placeholders like ADJECTIVE, NOUN, ADVERB, or VERB with user input.
import re

#read the contents of the text file
with open("files/input.txt", "r") as file:
    content = file.read()
    
# find al the placeholders in the text
placeholders = re.findall(r"ADJECTIVE|NOUN|ADVERB|VERB", content)

# replae each place holder with user input
for word in placeholders:
    article = "an" if word[0] in "AEIOU" else "a"
    user_input = input(f"Enter {article} {word.lower()}: ")
    content = content.replace(word, user_input, 1)
    
# print and save the modified content
print("\nModified content:")
print(content)

with open("files/madlibs_output.txt", "w") as file:
    file.write(content)