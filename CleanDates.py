import re

text = """
Dates to clean up: 3/14/2015, 03-14-2015, 2015/3/14, and 2015-03-14.
"""

# Regular expression patterns to match different date formats
date_pattern1 = r'(\d{1,2})/(\d{1,2})/(\d{4})'  # Matches M/D/YYYY and MM/DD/YYYY
date_pattern2 = r'(\d{4})/(\d{1,2})/(\d{1,2})'  # Matches YYYY/M/D and YYYY/MM/DD
date_pattern3 = r'(\d{1,2})-(\d{1,2})-(\d{4})'  # Matches M-D-YYYY and MM-DD-YYYY

# Replacement function to standardize the date format
def replace_date(match):
    parts = match.groups()
    if len(parts[0]) == 4:  # YYYY/MM/DD
        return f"{parts[0]}-{int(parts[1]):02d}-{int(parts[2]):02d}"
    return f"{parts[2]}-{int(parts[0]):02d}-{int(parts[1]):02d}"

# Substitute dates with the standard format
cleaned_text = re.sub(date_pattern1, replace_date, text)
cleaned_text = re.sub(date_pattern2, replace_date, cleaned_text)
cleaned_text = re.sub(date_pattern3, replace_date, cleaned_text)

print("Cleaned text:", cleaned_text)
