# # program for calculator
# print("       MINI---CALCULATOR")
# num1 = float(input("Enter your first number here:"))
# num2 = float(input("Enter your second number here:"))
# print("  1:ADD \n  2:SUB\n  3:MUL\n  4:DIV")
# choice = int(input("enter your choice "))
# if choice ==1:
#  print(num1 +num2)
# elif choice ==2:
#  print(num1-num2)
# elif choice==3:
#  print(num1*num2)
# elif choice==4:
#  print(num1/num2)
# else:
#  print("invalid input")


def calculator():
 try:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  print("Select operation: +, -, *, /")
  operation = input("Enter operation: ")
  if operation == '+':
   result = num1 + num2
  elif operation == '-':
   result = num1 - num2
  elif operation == '*':
   result = num1 * num2
  elif operation == '/':
   if num2 == 0:
    print("Error: Division by zero is not allowed.")
    return
   result = num1 / num2
  else:
   print("Invalid operation! Please choose +, -, *, or /.")
   return
  print(f"Result: {num1} {operation} {num2} = {result}")
 except ValueError:
  print("Invalid input! Please enter numeric values.")
calculator()






