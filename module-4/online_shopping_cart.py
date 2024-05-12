'''
Create a custom float formatting that formats the floating point numbers, as required by the problem, 
without supressing any precision if present.
'''
def format_float(num):
    if num == int(num):
        return str(int(num))
    else:
        return str(num)


# Step 1: Build the ItemToPurchase class

class ItemToPurchase:

    # Default constructor
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        # Initialize attributes
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Method
    def print_item_cost(self):
        """
        Prints the cost of the item in the format:
        "item_name item_quantity @ $item_price = $total_cost"
        """
        total_cost = self.item_price * self.item_quantity
        #Suppresing 
        print(f"{self.item_name} {self.item_quantity} @ ${format_float(self.item_price)} = ${format_float(total_cost)}")



# Step 2: Prompt the user for two items and create two objects of the ItemToPurchase class

# Prompt for Item 1
print("Item 1")

item1 = ItemToPurchase()
item1.item_name = input("Enter the item name:\n")
item1.item_price = float(input("Enter the item price:\n"))
item1.item_quantity = int(input("Enter the item quantity:\n"))

# Prompt for Item 2
print("\nItem 2")

item2 = ItemToPurchase()
item2.item_name = input("Enter the item name:\n")
item2.item_price = float(input("Enter the item price:\n"))
item2.item_quantity = int(input("Enter the item quantity:\n"))

# Step 3: Add the costs of the two items together and output the total cost

# Print total cost
print("\nTOTAL COST")

# Print cost of Item 1
item1.print_item_cost()

# Print cost of Item 2
item2.print_item_cost()

# Calculate total cost
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"Total: ${format_float(total_cost)}")