#To find URLs that begin with http:// or https://
import re 

text = """
Check out these websites: http://example.com and https://www.example.org.
Also, visit http://example.net for more information.
"""
# Regular expression pattern to find URLs
# url_pattern = re.compile(r"https?://\s+")

# url_pattern = r'https?://\S+'

# Find all URLs in the text
# urls = re.findall(url_pattern, text)

# print("Found URLs:", urls)


urlRegex = re.compile(r"https?://\S+")
urls = urlRegex.findall(text)

print("found urls : ", urls)
