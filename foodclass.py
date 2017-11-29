import itertools

class Food():
	#newid = itertools.count().next
	def __init__(self, name, price, quantity, chilled):	
		#self.id = Food.newid()
		self.name = name
		self.price = price
		self.quantity = quantity
		self.chilled = chilled
		
		print "A food was created. Its name is " + self.name + ", it costs " + \
		str(self.price) + " dollars, we are buying " + str(self.quantity) + \
		" of them, and its chilled value is " + str(self.chilled) + "."
	def __call__(self):
		print "bip bip I cost " + str(self.price) + " dollars!"

def yn_tf(b):
	if b == "y":
		return True
	else:
		return False
	
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
		food_dict[i]()
if __name__ == "__main__":
	main()
