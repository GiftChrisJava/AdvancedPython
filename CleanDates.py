import re

# Sample text containing dates in different formats
text = """
Dates to clean up: 3/14/2015, 03-14-2015, 2015/3/14, and 2015-03-14.
"""

# Regular expression pattern for M/D/YYYY and MM/DD/YYYY
date_pattern1 = r'(\d{1,2})/(\d{1,2})/(\d{4})'
# (\d{1,2}) - Matches 1 or 2 digits for the month
# / - Matches a forward slash
# (\d{1,2}) - Matches 1 or 2 digits for the day
# / - Matches a forward slash
# (\d{4}) - Matches exactly 4 digits for the year

# Regular expression pattern for YYYY/M/D and YYYY/MM/DD
date_pattern2 = r'(\d{4})/(\d{1,2})/(\d{1,2})'
# (\d{4}) - Matches exactly 4 digits for the year
# / - Matches a forward slash
# (\d{1,2}) - Matches 1 or 2 digits for the month
# / - Matches a forward slash
# (\d{1,2}) - Matches 1 or 2 digits for the day

# Regular expression pattern for M-D-YYYY and MM-DD-YYYY
date_pattern3 = r'(\d{1,2})-(\d{1,2})-(\d{4})'
# (\d{1,2}) - Matches 1 or 2 digits for the month
# - - Matches a hyphen
# (\d{1,2}) - Matches 1 or 2 digits for the day
# - - Matches a hyphen
# (\d{4}) - Matches exactly 4 digits for the year

# Replacement function to standardize the date format
def replace_date(match):
    parts = match.groups()  # Get matched groups as a tuple
    if len(parts[0]) == 4:  # Check if the first part is the year (4 digits)
        return f"{parts[0]}-{int(parts[1]):02d}-{int(parts[2]):02d}"
    # Standardize format to YYYY-MM-DD
    return f"{parts[2]}-{int(parts[0]):02d}-{int(parts[1]):02d}"

# Substitute dates with the standard format
cleaned_text = re.sub(date_pattern1, replace_date, text)
cleaned_text = re.sub(date_pattern2, replace_date, cleaned_text)
cleaned_text = re.sub(date_pattern3, replace_date, cleaned_text)

# Print the cleaned text
print("Cleaned text:", cleaned_text)
