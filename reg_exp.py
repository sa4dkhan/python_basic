"""
import re

name_age = '''
Janice is 22 and Theon is 33 
Gabriel is 44 and Joey is 21
'''

ages = re.findall(r'\d{1,3}', name_age)
names = re.findall(r'[A-Z][a-z]*', name_age)

age_dict = {}

x = 0

for eachname in names:
	age_dict[eachname] = ages[x]
	x += 1

print(age_dict)
"""


"""
import re


if re.search("inform", "we need to inform him with the latest information"):
	print("There is inform")


allinform = re.findall("inform", "we need to inform him with the latest information")

for i in allinform:
	print(i)
"""

"""
import re


str = "we need to inform him with the latest information"

for i in re.finditer("inform", str):
	loctup = i.span()
	print(loctup) 
"""


"""
import re


str = "Sat, hat mat, pat"

allstr = re.findall("[Shmp]at", str)

for i in allstr:
	print(i)
"""


import re


pattern = "Cookie"
sequence = "Cookie"

if re.match(pattern, sequence):
	print("Match!")

else:
	print("Not a match!")

x =re.search(r'Co.k.e', 'baal').group()

print(x)


















 

















