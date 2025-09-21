# This class defines a single item for a shopping cart.
class ItemToPurchase:
    """
    Represents an item to be purchased with a name, price, quantity, and description.
    """
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        """
        Initializes the item with a name, price, quantity, and description.
        The default constructor sets the values to "none", 0.0, 0, and "none".
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        """
        Calculates and prints the cost of the item.
        Example: Bottled Water 10 @ $1 = $10
        """
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

# This class defines the shopping cart and its methods.
class ShoppingCart:
    """
    Represents a shopping cart with a customer's name, date, and a list of items.
    """
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """
        Initializes the shopping cart with a customer name, date, and an empty list of items.
        """
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        """
        Adds an item to the cart_items list.
        """
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        """
        Removes an item from the cart_items list by name.
        """
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        """
        Modifies an item's quantity in the cart.
        """
        found = False
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_to_purchase.item_name:
                found = True
                # Only modify if the new quantity is not the default value.
                if item_to_purchase.item_quantity != 0:
                    self.cart_items[i].item_quantity = item_to_purchase.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """
        Returns the total quantity of all items in the cart.
        """
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        """
        Calculates and returns the total cost of all items in the cart.
        """
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        """
        Outputs the total of objects in the cart.
        """
        print("TOTAL COST")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            total_cost = 0
            for item in self.cart_items:
                item_total = item.item_price * item.item_quantity
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item_total:.2f}")
                total_cost += item_total
            print(f"Total: ${total_cost:.2f}")

    def print_descriptions(self):
        """
        Outputs each item's description.
        """
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart):
    """
    Prints a menu of options to manipulate the shopping cart.
    """
    menu_options = {
        'a': 'Add item to cart',
        'r': 'Remove item from cart',
        'c': 'Change item quantity',
        'i': "Output items' descriptions",
        'o': 'Output shopping cart',
        'q': 'Quit'
    }

    while True:
        print("\nMENU")
        for key, value in menu_options.items():
            print(f"{key} - {value}")

        choice = input("Choose an option: ").lower().strip()

        if choice == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            item_to_modify = ItemToPurchase(item_name, item_quantity=new_quantity)
            cart.modify_item(item_to_modify)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            print("QUIT")
            break
        else:
            print("Invalid choice. Please try again.")


# Main program section
if __name__ == "__main__":
    
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()

    # Create a ShoppingCart object with the user's name and date.
    shopping_cart = ShoppingCart(customer_name, current_date)
    
    # Call the main menu function.
    print_menu(shopping_cart)
