import re

# Sample text containing sensitive information
text = """
Sensitive info: SSN 123-45-6789, credit card 4111-1111-1111-1111.
"""

# Regular expression pattern for Social Security Number (SSN)
ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
# \b - Word boundary
# \d{3} - Matches exactly three digits
# - - Matches a hyphen
# \d{2} - Matches exactly two digits
# - - Matches a hyphen
# \d{4} - Matches exactly four digits
# \b - Word boundary

# Regular expression pattern for credit card number
cc_pattern = r'\b\d{4}-\d{4}-\d{4}-\d{4}\b'
# \b - Word boundary
# \d{4} - Matches exactly four digits
# - - Matches a hyphen
# \d{4} - Matches exactly four digits
# - - Matches a hyphen
# \d{4} - Matches exactly four digits
# - - Matches a hyphen
# \d{4} - Matches exactly four digits
# \b - Word boundary

# Substitute SSN with asterisks
cleaned_text = re.sub(ssn_pattern, '***-**-****', text)

# Substitute credit card number with asterisks
cleaned_text = re.sub(cc_pattern, '****-****-****-****', cleaned_text)

# Print the cleaned text
print("Cleaned text:", cleaned_text)
