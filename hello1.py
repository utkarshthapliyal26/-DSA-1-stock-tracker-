inventory = {}

def insert_product():
    skus_input = input("Enter SKU(s) (comma-separated for multiple): ")
    names_input = input("Enter Name(s) (comma-separated for multiple): ")
    quantities_input = input("Enter Quantity(ies) (comma-separated for multiple): ")

    skus = [s.strip() for s in skus_input.split(',')]
    names = [n.strip() for n in names_input.split(',')]
    quantities_str = [q.strip() for q in quantities_input.split(',')]

    if len(skus) != len(names) or len(skus) != len(quantities_str):
        print("Error: The number of SKUs, names, and quantities must match.")
        return

    for i in range(len(skus)):
        sku = skus[i]
        name = names[i]
        quantity_str = quantities_str[i]

        if not sku:
            print("Error: SKU cannot be empty.")
            continue
        if sku in inventory:
            print(f"Error: SKU '{sku}' already exists. Rejecting.")
            continue
        if not name:
            print("Error: Product name cannot be empty.")
            continue
        
        try:
            quantity = int(quantity_str)
            if quantity < 0:
                print("Error: Quantity must be positive.")
                continue
        except ValueError:
            print("Error: Invalid quantity. Please enter a whole number.")
            continue

        inventory[sku] = {'name': name, 'quantity': quantity}
        print(f"Product '{name}' with SKU '{sku}' inserted successfully.")

def delete_product():
    sku = input("Enter the SKU of the product to delete: ")
    if sku in inventory:
        removed_product = inventory.pop(sku)
        print(f"Product {removed_product['name']} removed from inventory.")
    else:
        print("Error: Product with that SKU not found.")

def search_product():
    choice = input("Search by (1) SKU or (2) Name? ")
    found = False
    if choice == '1':
        sku = input("Enter SKU to search for: ")
        if sku in inventory:
            product = inventory[sku]
            print("\n--- Product Found ---")
            print(f"SKU: {sku}")
            print(f"Name: {product['name']}")
            print(f"Quantity: {product['quantity']}")
            print("---------------------\n")
            found = True
    elif choice == '2':
        name = input("Enter Name to search for: ")
        for sku, product in inventory.items():
            if product['name'].lower() == name.lower():
                print("\n--- Product Found ---")
                print(f"SKU: {sku}")
                print(f"Name: {product['name']}")
                print(f"Quantity: {product['quantity']}")
                print("---------------------\n")
                found = True
    else:
        print("Invalid choice.")
        return

    if not found:
        print("Product not found.")

def display_inventory():
    print("\n==================== CURRENT INVENTORY ====================")
    if not inventory:
        print("Inventory is empty.")
    else:
        print(f"{'SKU':<15}{'Product Name':<20}{'Quantity':<10}")
        print("-" * 45)
        for sku, product in inventory.items():
            print(f"{sku:<15}{product['name']:<20}{product['quantity']:<10}")
    print("=========================================================\n")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product(s)")
        print("2. Delete Product")
        print("3. Search Product")
        print("4. Display Inventory")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            insert_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            search_product()
        elif choice == '4':
            display_inventory()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
