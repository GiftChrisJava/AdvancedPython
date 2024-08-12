import re

text = """
This is  a    text  with  multiple  spaces, repeated repeated words, and annoying exclamation marks!!!
"""

# Patterns for common typos
multiple_spaces_pattern = r'\s{2,}'       # Matches two or more spaces
repeated_words_pattern = r'\b(\w+)\s+\1\b'  # Matches repeated words
exclamation_pattern = r'!{2,}'            # Matches two or more exclamation marks

# Substitute multiple spaces with a single space
text = re.sub(multiple_spaces_pattern, ' ', text)

# Substitute repeated words with a single instance
text = re.sub(repeated_words_pattern, r'\1', text)

# Substitute multiple exclamation marks with a single exclamation mark
text = re.sub(exclamation_pattern, '!', text)

print("Cleaned text:", text)
