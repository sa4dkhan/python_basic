### Inheritance ###
'''
class Animal():
	
	def __init__(self):
		print("Animal Created")

	def who_am_i(self):
		print("Animal")
	
	def eat(self):
		print("Eating")

class Dog(Animal):
	
	def __init__(self):
		# Animal.__init__(self)
		print("Dog Created")
	
	def bark(self):
		print("Woof")
	
	def eat(self):
		print("Dog eating")

	

# my_a = Animal()
# my_a.who_am_i()
# my_a.eat()

my_d = Dog()
my_d.who_am_i()
my_d.eat() 
my_d.bark()

'''

### Special Methods ###

class Book():
	
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages
				
	def __str__(self):
		return "Title {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

	def __len__(self):
		return self.pages

	def __del__(self):
		print("A book is destroyed")	

b = Book("Python", "Saad", 200)

# print(b)
# print(len(b))

del b
print(b)
	


























