'''
Problem Statement:
Write a Python program to find the addition and subtraction of two numbers.

Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. Also, subtract the two numbers to find the output.
'''

'''
Pseudo-code:
1. Prompt the user to enter the first number (num1)
2. Prompt the user to enter the second number (num2)
3. Add num1 and num2 to find the sum
4. Subtract num2 from num1 to find the difference
5. Print the sum and difference
'''

# Prompting the user to enter the first number (num1)
num1 = float(input("Enter the first number: "))

# Prompting the user to enter the second number (num2)
num2 = float(input("Enter the second number: "))

# Adding num1 and num2
sum_result = num1 + num2

# Subtracting num2 from num1 to find the difference
difference_result = num1 - num2

# Printing the sum and difference
print("Addition result:", sum_result)
print("Subtraction result:", difference_result)
