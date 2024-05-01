'''
Pseudo-code:

START

INPUT food_charge

SET tip = food_charge * 0.18
SET sales_tax = food_charge * 0.07
SET total_price = food_charge + tip + sales_tax

OUTPUT food_charge
OUTPUT tip
OUTPUT sales_tax
OUTPUT total_price

END

'''

# Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip (18%)
tip = food_charge * 0.18

# Calculate the sales tax (7%)
sales_tax = food_charge * 0.07

# Calculate the total price
total_price = food_charge + tip + sales_tax

# Display the results
print(f"Food charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales tax (7%): ${sales_tax:.2f}")
print(f"Total price: ${total_price:.2f}")
