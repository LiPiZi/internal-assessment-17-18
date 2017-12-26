
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
		
		print("A food was created. Its name is " + self.name + ", it costs " + \
		str(self.price) + " dollars, we are buying " + str(self.quantity) + \
		" of them, and its chilled value is " + str(self.chilled) + ".")
	#for some reason, the dictionaries only let me use __call__
	def __call__(self, n):
		if n == 1:
			return self.name
		if n == 2:
			return self.price
	def henlo():
		print("bibo")
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
	expanded_food_price = {"Bagel1":1.99,"Bagel2":1.99,"Bagel3":1.99,"Nutella":3.99, "Spaghett":2.99}
	expanded_food_chillded_price = {"Milk1":2.99,"Milk1":2.99}
	person_dict = {"Jack": False, "Jill":False, "Feebo":True}
	total_price = 0.0
	for k,v in expanded_food_price.items():
		total_price += v
	print(total_price)
	avg_price = total_price/(len(person_dict))
	avg_price = int(avg_price*100)/100.00
	print(avg_price)
	
	person_list = []
	person_chilled_list = []
	for a,b in person_dict.items():
		if b == False:
			person_list.append(a)
		else:
			person_chilled_list.append(a)
	
	print(person_list)
	print(person_chilled_list)

	expanded_by_cent = []
	
	for k, v in expanded_food_price.items():
		i = 0
		while i < int(v*100):
			expanded_by_cent.append([k])
			i += 1
	print(expanded_by_cent)
	i = 0
	iterate_to = int(avg_price*100)
	person_amnt_dict = {}
	print(len(expanded_by_cent))
	while i<len(person_list):
		cent_list_for_person = []
		while b<iterate_to:
			cent_list_for_person.append(expanded_by_cent[b])
			b+=1
		person_amnt_dict.update({person_list[i]:cent_list_for_person})
		i+=1
		iterate_to += int(avg_price*100)
	print(person_amnt_dict.items())
	
	print(len(person_amnt_dict["Jack"]), len(person_amnt_dict["Jill"]))
	
if __name__=="__main__":
	main()
