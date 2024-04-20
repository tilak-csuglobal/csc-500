'''
Problem Statement:
Write a Python program to find the multiplication and division of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output.
'''

'''
Pseudo-code:
1. Prompt the user to enter the first number (num1)
2. Prompt the user to enter the second number (num2)
3. Multiply num1 and num2 to find the product
4. If num2 is not zero, divide num1 by num2 to find the quotient
5. If num2 is zero, set the quotient result to "Cannot divide by zero"
6. Print the product and quotient results
'''

# Prompting the user to enter the first number (num1)
num1 = float(input("Enter the first number: "))

# Prompting the user to enter the second number (num2)
num2 = float(input("Enter the second number: "))

# Multiplying num1 and num2 to find the product
product_result = num1 * num2

# Dividing num1 by num2 to find the quotient
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Cannot divide by zero"

# Printing the product and quotient results
print("Multiplication result:", product_result)
print("Division result:", quotient_result)

