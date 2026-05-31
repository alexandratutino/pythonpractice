class Math :
	def __init__(self,x,y) :
		self.x = x
		self.y = y 

	def Add(self) :
		z = self.x + self.y 
		print(f"{x} + {y} = {z}")

	def Subtract(self) :
		z = self.x - self.y 
		print(f"{x} - {y} = {z}")

	def Multiply(self) :
		z = self.x * self.y 
		print(f"{x} * {y} = {z}")

	def Divide(self) :
		if self.y == 0 :
			print("Cannot divide these two numbers as y = 0.")
		else :
			z = self.x / self.y 
			print(f"{x} / {y} = {z}")

x = float(input("Welcome, please enter a number for value x : "))
y = float(input("Welcome, please enter a number for value y : "))

values = Math(x,y)

values.Add()
values.Subtract()
values.Multiply()
values.Divide()