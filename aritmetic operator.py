# program to perform aritmetic operation based on user input
# taking number from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/): ")
# performing operation
if  operator == "+":
   result = num1 + num2
   print("Result=",result)
elif  operator == "-":
   result = num1 - num2
   print("Result=",result)
elif  operator == "*":
   result = num1 * num2
   print("Result=",result)
elif  operator == "/":
     if num2 != 0:
        result = num1 / num2

print("Result=",result)

