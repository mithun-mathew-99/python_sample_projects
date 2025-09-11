def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	if b == 0:
		return "Error. Divition by zero not possible"
	return x/y
print("===Simple Calculator===")
print("Choose operation")
print("1. ADD +")
print("2. SUBTRACT -")
print("3. MULTIPLY *")
print("4. DIVIDE /")

op = input("Enter you choice (symbol +,-,*,/) :")
a = float(input("Enter first number: \n"))
b = float(input("Enter second number: \n"))

if op == '+':
	result = add(a,b)
elif op == '-':
	result = subtract(a,b)
elif op == '*':
	result = multiply(a,b)
elif op == '/':
	result = divide(a,b)
else:
	result = "Invalid operator"

print("Result ---> ", result)