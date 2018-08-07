# Given the string

s = 'django'

# Use indexing to print out the following

print(s[0])
print(s[5]) # or print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4::]) # or print(s[4:])

### Bonus: Use indexing to reverse the string
print(s[::-1])


### Problem 2 ###
### Given this nested list: ###
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)


#### Problem 3 ####
### Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])


######## Problem 4 #####

mylist = [1,1,1,1,1,1,3,3,3,3,3,3,2,2,2,2,2]
unique = set(mylist)
print(unique)

###### Problem 5 ########
### You are given two variables ###

age = 4
name = 'Sammy'

print("Hello my dog's name is {} and he is {} years old".format(name, age))