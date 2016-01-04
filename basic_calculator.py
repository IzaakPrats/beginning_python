x = int(input("Enter your first number: "))
y = int(input("Input your second number: "))
o = str(input("Enter the operator: "))

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y;

def multiply(x, y):
	return x * y;

def divide(x, y):
	return x / y;

if o is "+":
	print(str(add(x, y)))

if o is "-":
	print(str(subtract(x,y)))

if o is "*":
	print(str(multiply(x,y)))

if o is "/":
	print(str(divide(x,y)))