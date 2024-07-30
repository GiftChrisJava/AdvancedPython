import re

text = """
Sensitive info: SSN 123-45-6789, credit card 4111-1111-1111-1111.
"""

# Regular expression patterns for SSN and credit card numbers
ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
cc_pattern = r'\b\d{4}-\d{4}-\d{4}-\d{4}\b'

# Substitute sensitive information with asterisks
cleaned_text = re.sub(ssn_pattern, '***-**-****', text)
cleaned_text = re.sub(cc_pattern, '****-****-****-****', cleaned_text)

print("Cleaned text:", cleaned_text)
