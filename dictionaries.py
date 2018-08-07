# Dictionaries

# my_stuff = {'key1': 'value1', 'key2': 'value2', 'key3':{'123':[1,2,3, 'grabMe']}}
# print(my_stuff['key3']['123'][3].upper())

my_stuff = {'lunch': 'pizza', 'bfast': 'eggs'}

# print(my_stuff['lunch'])

### Dictionaries are immutable ###
my_stuff['lunch']  = 'burger'
# print(my_stuff['lunch'])

## Add to dictionaries ##
my_stuff['dinner'] = 'pasta'
print(my_stuff)



