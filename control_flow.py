### Comparison Operators ###

## Greater Than ##

1 > 2

## Less than ##

1 < 2

## Greater than or equal to

1 >= 1

## Less than or equal to

1 == 1

## Equality

1 == 1

## check if identical ##
1 == "1"

'hi' == 'bye'


## Inequality

1 != 2

### Logical Operators ###

## And

(1 > 2) and (2 < 3)

## Or 

(1 > 2) or (2 < 3)


## Multiple logical operators

(1 == 2) or (2 == 3) or (4 == 4)


## Condition if else elif statement
# if 1<2:
#	print('First Block')
#	if 20 < 3:
#       	print("True!")

'''
if 1 == 1:
	if 1 > 2:
		print("hello")
	elif 3 == 3:
		print('elif ran')
	else:
		print("last")

'''

### For Loops

sequence = [1,2,3,4,5,6]


'''
for item in sequence:
	print(item)
	print('hello')
'''


'''
names = {'Sam':1, 'Frank':2, 'Dan':3}

for name in names:
	print(name)
	print(names[name])
'''


###
# Here is a list of 3 tuples
'''
mypairs = [(1,2,3), (4,5,6), (7,8,9)]

for (tup1, tup2, tup3) in mypairs:
	print(tup1)
	print(tup2)

'''


### While Loops ###
'''
i = 1

while i<5:
	print("i is: {}".format(i))
	i = i + 1
'''

### Range function ###


# list = [1,2,3,4,5]


# print(list)
'''
a = range(7)
b = list(a)
print(b)


a = list(range(1,20,2))
print(a)


for item in range(1,10):
	print(item)

'''


### List Comprehension ###

lists = [1,2,3,4,5]

out = []

for number in lists:
	out.append(number**2)

print(out)

## or

out = [num**2 for num in lists]
print(out)


















































