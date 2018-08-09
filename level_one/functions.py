'''
def my_func(param1='Hello World'):
	"""
	This is the docstring
	"""
	print("my first python function is: {}!".format(param1))

my_func()
'''

"""
def hello():
	return "hello"

result = hello()

print(result)
"""

"""
def add_numb(num1, num2):
	if type(num1)==type(num2)==type(10): # ?
		return num1 + num2
	else:
		return "Sorry, I need integers!"

result = add_numb("2", "3") # add_numb("2", "3") will print 23
print(result)
"""


### Lambda expression ###

# Filter
"""
mylist = [1,2,3,4,5,6,7,8,9]

def even_bool(num):
	return num%2 == 0

def odd_bool(num):
	return num%2 == 1

evens = filter(even_bool, mylist)
odds = filter(odd_bool, mylist)
print(list(evens))
print(list(odds))
"""

# Lambda functions
"""
mylist = [1,2,3,4,5,6,7,8,9]
even = filter(lambda num:num%2 == 0, mylist)
print(list(even))
"""

"""
tweet = "Go Sports! #Sports"
result = tweet.split('#')[1]
print(result)
"""

# Check if x in list
"""
print('x' in [1, 2, 3, 'x'])
"""

































