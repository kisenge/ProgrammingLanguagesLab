#CS2613
#Python Test
#Driver Code
from Cat import *

user_in = ""

#TODO: Create a dictionary with all shelters as keys and lists of cats as values
catDictionary={}

while user_in != "X":
	print("A - Add a cat to a shelter")
	print("P - Print all the cats in a shelter")
	print("R - Do a role call in all shelters")
	print("X - Exit the program")
	user_in = input()


	if user_in == "A":
		print("Which shelter would you like to add a cat to?")
		shelter_name = input()

		#TODO: Add new shelters to the dictionary
		#catDictionary.update({shelter_name:})

		print("Input a cat's name, weight, and colour separated by a new line character")
		name = input()
		weight = float(input())
		colour = input()

		cat = Cat(name, weight, colour)

		
		#TODO: Add cat to list of cats at a specific shelter
		for key, val in catDictionary.items():
			if key==shelter_name:
				catDictionary.update({shelter_name:val.append(cat)})
			else:
				catDictionary.update({shelter_name:cat})


	elif user_in == "P":
		print("Which shelter would you like to print?")
		shelter_name = input()




		#TODO: Complete the Printing a Shelter functionality
		for key, val in catDictionary.items():
			if key==shelter_name:
				print(val.to_string())

		pass

	elif user_in == "R":
		#TODO: Complete the Role Call functionality
		pass

	elif user_in != "X":
		print("Invalid input")



