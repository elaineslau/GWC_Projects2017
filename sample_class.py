class Food:
	def __init__(self, name):
		self.name = name
		self.numcarbs = 0
		self.numcals = 0
		self.isHot = False
		self.ingredients = []

	def cook (self, cookTime):
		print ("It took " + cookTime + " to cook " + self.name + "!")
		self.isHot = True
		print ("The food is now hot!")

	def isItHot (self):
		return self.isHot	

def main ():
	Cookie = Food("Chocolate Chip")
	Cookie.cook("20 minutes")
	print (Cookie.isItHot())

	Apple = Food ("Granny Smith")
	Apple.cook ("3 hours")
	print (Apple.isItHot())

main()