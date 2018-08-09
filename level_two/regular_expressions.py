'''
import re

patterns = ['term1', 'term2']

text = "This is a string with term1, not the other!"

for pattern in patterns:
	print("I'm searching for: "+pattern)

	if re.search(pattern, text):
		print("Match")
	else:
		print("No match")
'''

import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"	