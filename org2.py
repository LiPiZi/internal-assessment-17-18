import collections
import sys

#from __future__ import print_function
import httplib2
import os
import requests

import mysql.connector

'''def send_simple_message(to, subject, text):
	return requests.post(
        "uri",
        auth=("api", "key"),
        data={"data",
              "to": to,
              "subject": subject,
              "text": text})'''
			  
class Person():
	def __init__(self, name, cooler, email):
		
		#self.id = id
		self.name = name
		self.cooler = cooler
		self.email = email
		
	def __call__(self, n):
		if n == 1:
			return self.name
		if n == 2:
			return self.cooler
		if n == 3:
			return self.email
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
		if n == 3:
			return self.quantity
		if n == 4:
			return self.chilled

def fiftybool(number):
	if number >= .5:
		return True
	else:
		return False
#yesno_truefalse
def yn_tf(b):
	if b == "y":
		return True
	else:
		return False

#This is its own thing and not an init because I might change the input method
def new_food():
	n = input("Enter a food name: ")
	
	p = float(input("Enter the price: "))
	
	q = int(input("Enter the number you're buying: "))
	
	c = False
	#yn_tf(input("Enter whether it is chilled (y/n): "))
	
	return Food(n, p, q, c)

def pick_food():
	food_list = []
	cont = True
	while cont == True:
		food_list.append(new_food())
		cont = yn_tf(input("Next food? (y/n)"))
	return food_list
	
def pick_person():
	person_list = []
	cont = True
	cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='orufood')
	cursor = cnx.cursor()
	query = "SELECT email, name FROM patron"
	cursor.execute(query)
	for (email, name) in cursor:
		go = yn_tf(input("is " + name + " going? (y/n)"))
		if go == True:
			c = yn_tf(input("does this person have a cooler? (y/n)"))
			newperson = Person(name, c, email)
			person_list.append(newperson)

	cursor.close()
	cnx.close()
	return person_list

	
def main():
	food_list = pick_food()
	person_list_initial = pick_person()
	
	
	expanded_food_price = collections.OrderedDict()
	expanded_food_chilled_price = collections.OrderedDict()
	
	for current_item in food_list:
		i = 0
		if current_item(4) == False:
			for i in range(current_item(3)):
				currstring = current_item(1) + ", number " + str(i+1) \
				+ " of " + str(current_item(3))
				expanded_food_price.update({currstring:current_item(2)}
				)
		if current_item(4) == True:
			for i in range(current_item(3)):
				currstring = current_item(1) + ", number " + str(i+1) \
				+ " of " + str(current_item(3))
				expanded_food_chilled_price.update(
				{currstring:current_item(2)})
	print(expanded_food_price.items())

	
	#calculate total price
	total_price = 0.0
	for k,v in expanded_food_price.items():
		total_price += v
	#put people in their lists
	person_list = []
	person_chilled_list = []
	for a in person_list_initial:
		if a(2) == False:
			person_list.append(a)
		else:
			person_chilled_list.append(a)
	#calculate and round average price
	print(person_list)
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
	#you should now be getting something like 'jack':['item1','item2',
	#'item2','item3'], 'jill':['item3','item3','item4'...]
	
	#consolidate or repack values into a dictionary in a dictionary
	current_list = 0
	current_person = 0
	person_price_dict = {}
	for current_person,current_list in person_amnt_dict.items():
		price_percent_dict = {}
		internal_iterator = 0
		last_item = current_list[0]
		print("\n",current_person(1)+":")
		#this should iterate through the current person's list
		while internal_iterator < len(current_list):
			current_counter = 0
			while current_list[internal_iterator] == last_item:
				current_counter += 1
				internal_iterator += 1
				sys.stdout.write('\r'+str(internal_iterator)+"/"+str(len(current_list)))
				'''this breaks it before an error. Probably something
				better exists.'''
				if internal_iterator >= len(current_list):
					break
			current_percent = current_counter/(expanded_food_price[last_item]*100)
			if internal_iterator < len(current_list):
				last_item = current_list[internal_iterator]
				#again, something better exists.
			price_percent_dict.update({current_list[internal_iterator-1]:current_percent})
		person_price_dict.update({current_person:price_percent_dict})
	'''intent: A dict of items that goes {Person:{Food1:percent, 
		food2:percent, food3:percent}} in person_price_dict'''
		
	#put all key items with a value>50% into list that goes inside dict
	person = 0
	current_dict = {}
	person_item_dict = {} #final output!
	for person,current_dict in person_price_dict.items():
		percent = 0
		item = 0
		item_list = []
		for item,percent in current_dict.items():
			include = fiftybool(percent)
			if include == True:
				item_list.append(item)
		person_item_dict.update({person:item_list})
	a=0
	b=0
	print("\n")
	email = "orufoodbot@gmail.com"
	subject = "Food to buy at the coming regatta:"
	for a,b in person_item_dict.items():
		content  = ("hello, " + a(1) + ". I am a robot, beep boop. you \
			have to buy: " + str(b))
		send_simple_message(a(3),subject, content)
		
	
	
if __name__=="__main__":
	main()
