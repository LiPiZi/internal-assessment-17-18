class Person():
	def __init__(self, id, name, cooler,):
		
		self.id = id
		self.name = name
		self.cooler = cooler
		
		
class Food():
	#The parts of the food
	def __init__(self, name, price, quantity, chilled):	
	
		self.name = name
		self.price = price
		self.quantity = quantity
		self.chilled = chilled
		
		print "A food was created. Its name is " + self.name + ", it costs " + \
		str(self.price) + " dollars, we are buying " + str(self.quantity) + \
		" of them, and its chilled value is " + str(self.chilled) + "."
	'''for some reason, the dictionaries only let me use __call__, so I jerry-rigged
	this guy to let me get all class params'''
	def __call__(self, n):
		if n == 1:
			return self.name
		if n == 2:
			return self.price

#yesno_truefalse
def yn_tf(b):
	if b == "y":
		return True
	else:
		return False

'''This is its own thing and not the food init because I might change the input method
	in the future.'''
def new_food():
	n = raw_input("Enter a name: ")
	
	p = float(input("Enter the price: "))
	
	q = int(input("Enter the number you're buying: "))
	
	c = yn_tf(raw_input("Enter whether it is chilled (y/n): "))
	
	return Food(n, p, q, c)
	
def main():
	cont = True
	food_dict = {}
	food_id = 0
	while cont == True:
		food_dict.update({food_id: new_food()})
		cont = yn_tf(raw_input("Continue? (y/n): "))
		food_id += 1
		
	for i in food_dict:
		print food_dict[i](1)
		print str(food_dict[i](2))
		
if __name__ == "__main__":
	main()
