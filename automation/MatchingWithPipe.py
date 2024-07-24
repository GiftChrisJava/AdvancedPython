import re

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo2 = heroRegex.search('Tina Fey and Batman.')

word2 = mo2.group()
word1 = mo1.group()

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo3 = batRegex.search("Batmobile lost a wheel")
word3 = mo3.group()
word4 = mo3.group(1)

print(word1, word2, word3, word4)
