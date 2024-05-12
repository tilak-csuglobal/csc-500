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

# Create a list to store the items
items = []

# Prompt user for two items
for i in range(2):
    print(f"\nItem {i+1}")
    item = ItemToPurchase()
    item.item_name = input("Enter the item name:\n")
    item.item_price = float(input("Enter the item price:\n"))
    item.item_quantity = int(input("Enter the item quantity:\n"))
    items.append(item)

# Print total cost
print("\nTOTAL COST")
total = 0
for item in items:
    item.print_item_cost()
    total += item.item_price * item.item_quantity
print(f"Total: ${format_float(total)}")