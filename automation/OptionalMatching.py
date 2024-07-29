import re

batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
# 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
# 'Batwoman'

# make the regex look for phone numbers that do or do not have an area code.

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
# '415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
# '555-4242'

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
# 'Batwowowowoman'

# Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
# 'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
# 'Batwowowowoman'
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
True

#Matching Specific Repetitions with Curly Brackets
haRegex = re.compile(r"(Ha){3,}")
laugh2 = haRegex.search("HaHaHa")

print(laugh2.group())


#Greedy and Nongreedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
# 'HaHaHaHaHa'
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
# 'HaHaHa'


# The findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()
# '415-555-9999