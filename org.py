import collections

class Person():
	def __init__(self, name, cooler,):
		
		#self.id = id
		self.name = name
		self.cooler = cooler
		
	def __call__(self, n):
		if n == 1:
			return self.name
		if n == 2:
			return self.cooler
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
	#for some reason, the dictionaries only let me use __call__
	def __call__(self, n):
		if n == 1:
			return self.name
		if n == 2:
			return self.price
	def henlo():
		print "bibo"
#yesno_truefalse
def yn_tf(b):
	if b == "y":
		return True
	else:
		return False

#This is its own thing and not an init because I might change the input method
def new_food():
	n = raw_input("Enter a food name: ")
	
	p = float(input("Enter the price: "))
	
	q = int(input("Enter the number you're buying: "))
	
	c = yn_tf(raw_input("Enter whether it is chilled (y/n): "))
	
	return Food(n, p, q, c)

def new_person():
	
	n = raw_input("Enter a person name: ")
	c = yn_tf(raw_input("Enter whether this person has a cooler (y/n): "))
	
	return Person(n, c)
	
def main():
	expanded_food_price = collections.OrderedDict()
	expanded_food_price = {"Bagel1":1.99,"Bagel2":1.99,"Bagel3":1.99,"Milk1":2.99,"Milk1":2.99}
	person_dict = {"Jack": True, "Jill":False}
	total_price = 0.0
	for k,v in expanded_food_price.items():
		total_price += v
	print total_price
	avg_price = total_price/(len(person_dict))
	avg_price = int(avg_price*100)/100.00
	print avg_price
	
	curr_person_price = 0.0
	curr_food_price = 0.0
	person_amnt_dict = {}
	
	for k,v in expanded_food_price.items():
		food_percent = 0
		while 

print person_amnt_dict["Jack"]		
if __name__ == "__main__":
	main()
