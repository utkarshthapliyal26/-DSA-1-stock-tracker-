# Inventory list to store product records
inventory = []

# Function to insert a new product
def insert_product():
    """Inserts a new product into the inventory list."""
    sku = input("Enter SKU: ")

    # Check for duplicate SKU
    for item in inventory:
        if item['sku'] == sku:
            print("Product with this SKU already exists!")
            return

    name = input("Enter Product Name: ")

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return 

    # Create product dictionary and add to inventory
    product = {'sku': sku, 'name': name, 'quantity': quantity}
    inventory.append(product)
    print("Product inserted successfully.")

# Function to display inventory
def display_inventory():
    """Displays the current products in the inventory."""
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\nCurrent Inventory:")
    print("SKU\t\tProduct Name\t\tQuantity")
    print("-----------------------------------------------")
    
    # The f-string was corrected here to properly display the product details.
    for item in inventory:
        print(f"{item['sku']}\t\t{item['name']}\t\t{item['quantity']}")
    
    print()

# Main program loop
def main():
    """Runs the main loop for the inventory manager application."""
    while True:
        print("\nInventory Stock Manager")
        print("1. Insert New Product")
        print("2. Display Inventory")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            insert_product()
        elif choice == '2': 
            display_inventory()
        elif choice == '3':
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice. Please select from 1 to 3.")

# This ensures the main function runs when the script is executed.
if __name__ == "__main__":
    main()
