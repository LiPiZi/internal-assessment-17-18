
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
	#These are a few things that will be made by other parts of the program.
	expanded_food_price = collections.OrderedDict()
	expanded_food_price = {"item1":0.02,"item2":0.02,"item3":0.03,"item4":0.04, "item5":0.05}
	expanded_food_chilled_price = {"Milk1":2.99,"Milk1":2.99}
	person_dict = {"Jack": False, "Jill":False, "Ernie":True}
	
	#calculate total price
	total_price = 0.0
	for k,v in expanded_food_price.items():
		total_price += v
	#put people in their lists
	person_list = []
	person_chilled_list = []
	for a,b in person_dict.items():
		print(a,b)
		if b == False:
			person_list.append(a)
		else:
			person_chilled_list.append(a)
	
	print(person_list)
	#calculate and round average price
	avg_price = total_price/(len(person_list))
	avg_price = int(avg_price*100)/100.00
	#avg_chilled_price = total_price/(len(person_chilled_list))
	#avg_chilled_price = int(avg_chilled_price*100)/100.00
	
	
	expanded_by_cent = []
	c = 0
	d = 0
	for c,d in expanded_food_price.items():
		i = 0
		while i < int(d*100):
			expanded_by_cent.append(c)
			i += 1
	
	i = 0
	b = 0
	iterate_to = int(avg_price*100)
	person_amnt_dict = {}
	
	while i<len(person_list):
		cent_list_for_person = []
		while b<iterate_to:
			cent_list_for_person.append(expanded_by_cent[b])
			b+=1
		person_amnt_dict.update({person_list[i]:cent_list_for_person})
		i+=1
		iterate_to += int(avg_price*100)
	
	print(person_amnt_dict.items())
if __name__=="__main__":
	main()