number1 = int(input("enter the first number: "))
operator = input(" enter an operator: ")
number2 = int(input("enter a second number: "))
if operator == "+":
	total = number1 + number2
	print(f"{number1} + {number2} = {total}")
elif operator == "-":
	total = number1 - number2
	print(f"{number1} - {number2} = {total}")

elif operator == "*":
	total = number1 * number2
	print(f"{number1} * {number2} = {total}")	

elif operator == "/":
	total = number1 / number2
	print(f"{number1} / {number2} = {total}")	

elif operator == "**":
	total = number1 ** number2
	print(f"{number1} ** {number2} = {total}")

elif operator == "//":
	total = number1 // number2
	print(f"{number1} // {number2} = {total}")	

elif operator == "%":
	total = number1 % number2
	print(f"{number1} % {number2} = {total}")	