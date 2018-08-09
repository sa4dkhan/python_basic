class Circle():
	pi = 3.14 # attribute
	def __init__(self, radius= 1):
		self.radius = radius

	def area(self):
		return self.radius*self.radius * Circle.pi

	def set_radius(self, new_r):
		self.radius = new_r

my_c = Circle(3)
my_c.set_radius(999)
print(my_c.area())