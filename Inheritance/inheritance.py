class Parent():
	"""Parent"""
	def __init__(self, last_name, eye_color):
		#print("Parent const called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last Name is: " + self.last_name)
		print("Eye Color is: " + self.eye_color)
		

class Child(Parent):
	"""docstring for Child"""
	def __init__(self,last_name, eye_color, no_of_toys):
		#print("Child inst called")
		Parent.__init__(self,last_name,eye_color)
		self.no_of_toys = no_of_toys

	def show_info(self):
		print("Last Name is: " + self.last_name)
		print("Eye Color is: " + self.eye_color)
		print("Number of toys are: " + str(self.no_of_toys))
		

Piyush_maheheshwari = Parent("Maheshwari", "Black")
#Piyush_maheheshwari.show_info()
Siddhanth = Child("Maheshwari","Black","5")
Siddhanth.show_info()
#print(Siddhanth.last_name)
#print(Siddhanth.no_of_toys)