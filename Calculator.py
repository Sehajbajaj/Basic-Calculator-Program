#To make a simple calculator in python

#function for addition
def add(x , y):
    return x + y

#function for subtraction
def subtract(x , y):
    return x - y

#function for multiplication
def multiply(x , y):
    return x * y

#function for division
def divide(x , y):
    return x / y

print("Please select operation: \n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

menu = int(input("Select operation from 1, 2, 3, 4, :"))
num1 = float(input("Enter first number: "))
num2 = float(input("ENter second number: "))

if menu == 1:
    print(num1 , " + " , num2 , "=", add(num1 , num2))
elif menu == 2:
    print(num1 , " - " , num2 , "=", subtract(num1 , num2))
elif menu == 3:
    print(num1 , " * " , num2 , "=", multiply(num1 , num2))
elif menu == 4:
    print(num1 , " / " , num2 , "=", divide(num1 , num2))
else:
    print("Invalid Output")
