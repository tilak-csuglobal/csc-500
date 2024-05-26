# Step 0: Leveraging the code for ItemToPurchase class developed during Module 4, with an additional instance variable- item_description

class ItemToPurchase:

    # Default constructor
    def __init__(self, item_name="none", item_description="", item_price=0.0, item_quantity=0):
        # Initialize attributes
        self.item_name = item_name
        self.item_description = item_description
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

# Step 4: Build the ShoppingCart class. Module-6 assignment begins here

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # Initialize an empty list to store items

    def add_item(self, item):
        """
        Adds an item to the cart_items list.
        :param item: An instance of ItemToPurchase
        """
        self.cart_items.append(item) # Add the item to the cart_items list

    def remove_item(self, item_name):
        """
        Removes an item from the cart_items list.
        :param item_name: The name of the item to be removed
        """
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item) # Remove the item from the cart_items list
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        """
        Modifies an item's description, price, and/or quantity.
        :param modified_item: An instance of ItemToPurchase with updated values
        """
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                # Check if the item has default value for item_description
                if modified_item.item_description != "":
                    item.item_description = modified_item.item_description
                # Check if the item has default value for item_price
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                # Check if the item has default value for item_quantity
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.") # Print a message if the item is not found

    def get_num_items_in_cart(self):
        # Returns the total quantity of all items in the cart.
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        # Determines and returns the total cost of items in the cart.
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        # Outputs the total items in the cart.
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost}" if total_cost > 0 else "SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        # Outputs each item's description.
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

# Step 5: Implement the print_menu() function

def print_menu(cart):
    """
    Outputs a menu of options to manipulate the shopping cart.
    :param cart: An instance of ShoppingCart
    """
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = str.lower(input("Choose an option:\n"))

        if choice == 'a':
            # Implement adding an item to the cart
            pass
        elif choice == 'r':
            # Implement removing an item from the cart
            pass
        elif choice == 'c':
            # Implement changing item quantity
            pass
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice, please try again.")

# Step 6: Implement Output shopping cart and Output item's description menu options

def main():
    #  Sample Usage
    my_cart = ShoppingCart("John Doe", "February 1, 2020")
    item1 = ItemToPurchase("Nike Romaleos 2", "Volt color, Weightlifting shoes", 189, 1)
    item2 = ItemToPurchase("Chocolate Chips", "Semi-sweet", 3, 5)
    item3 = ItemToPurchase("Powerbeats 2 Headphones", "Bluetooth headphones", 128, 1)
    my_cart.add_item(item1)
    my_cart.add_item(item2)
    my_cart.add_item(item3)

    print_menu(my_cart)


# Run the main function
if __name__ == "__main__":
    main()