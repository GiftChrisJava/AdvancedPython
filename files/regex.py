# This program searches through all .txt files in a folder for lines
# that match a user-supplied regular expression. 

import os
import re

# Prompt the user for a regular expression.
regex_pattern = input('Enter a regular expression: ')
regex = re.compile(regex_pattern)

# Search all text files in the current directory.
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if regex.search(line):
                    print(f'Found in {filename}, line {line_num}: {line.strip()}')
