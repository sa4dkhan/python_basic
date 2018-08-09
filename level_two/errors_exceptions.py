### with exceptions ###

try:
	f = open('simple.txt', 'r')
	f.write("Test write to simple text!")

# IOError is optional for this case
except IOError: 
	print("Error: could not find file or read data")


else:
	print("Success")
	f.close()

finally:
	print("I always work no matter what!")

print("hello world")


### without exception ###
'''
f = open('simple.txt', 'r')
f.write("Test write to simple text!")

print("hello world")
'''