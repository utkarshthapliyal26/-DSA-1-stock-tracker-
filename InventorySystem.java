import java.util.ArrayList;
import java.util.Scanner;

// Class to represent a Product
class Product {
    String sku;     // e.g., P101
    String name;    // Product name
    int quantity;   // Quantity (must be positive)

    // Constructor
    Product(String sku, String name, int quantity) {
        this.sku = sku;
        this.name = name;
        this.quantity = quantity;
    }
}

public class InventorySystem {
    static ArrayList<Product> inventory = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    // Check if SKU already exists
    public static boolean skuExists(String sku) {
        for (Product p : inventory) {
            if (p.sku.equalsIgnoreCase(sku)) {
                return true;
            }
        }
        return false;
    }

    // Function to create a product
    public static Product createProduct() {
        System.out.print("Enter SKU : ");
        String sku = sc.next();

        if (skuExists(sku)) {
            System.out.println("Error: Duplicate SKU! Product rejected.");
            return null;
        }

        sc.nextLine(); // consume newline
        System.out.print("Enter Product Name: ");
        String name = sc.nextLine().trim();

        if (name.isEmpty()) {
            System.out.println("Error: Product name cannot be empty!");
            return null;
        }

        System.out.print("Enter Quantity: ");
        if (!sc.hasNextInt()) {
            System.out.println("Error: Invalid quantity (must be a number).");
            sc.next(); // clear invalid input
            return null;
        }
        int qty = sc.nextInt();

        if (qty <= 0) {
            System.out.println("Error: Quantity must be positive!");
            return null;
        }

        return new Product(sku, name, qty);
    }

    // Insert product into inventory
    public static void insertProduct(Product p) {
        if (p != null) {
            inventory.add(p);
            System.out.println("Product added successfully!");
        }
    }

    // Display inventory
    public static void displayInventory() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty!");
            return;
        }
        System.out.println("\n--- Inventory ---");
        for (Product p : inventory) {
            System.out.println("SKU: " + p.sku + ", Name: " + p.name + ", Quantity: " + p.quantity);
        }
    }

    // Search product by SKU
    public static void searchBySKU(String sku) {
        for (Product p : inventory) {
            if (p.sku.equalsIgnoreCase(sku)) {
                System.out.println("Product Found -> SKU: " + p.sku + ", Name: " + p.name + ", Quantity: " + p.quantity);
                return;
            }
        }
        System.out.println("Error: Product with SKU " + sku + " not found.");
    }

    // Search product by Name
    public static void searchByName(String name) {
        for (Product p : inventory) {
            if (p.name.equalsIgnoreCase(name)) {
                System.out.println("Product Found -> SKU: " + p.sku + ", Name: " + p.name + ", Quantity: " + p.quantity);
                return;
            }
        }
        System.out.println("Error: Product with Name " + name + " not found.");
    }

    // Delete product by SKU
    public static void deleteProduct(String sku) {
        for (Product p : inventory) {
            if (p.sku.equalsIgnoreCase(sku)) {
                inventory.remove(p);
                System.out.println("Product " + p.name + " removed from inventory.");
                return;
            }
        }
        System.out.println("Error: Product with SKU " + sku + " not found.");
    }

    // Main loop
    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("\nInventory Menu:");
            System.out.println("1. Add Product");
            System.out.println("2. Display Inventory");
            System.out.println("3. Search by SKU");
            System.out.println("4. Search by Name");
            System.out.println("5. Delete Product by SKU");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    Product p = createProduct();
                    insertProduct(p);
                    break;
                case 2:
                    displayInventory();
                    break;
                case 3:
                    System.out.print("Enter SKU to search: ");
                    String sku = sc.next();
                    searchBySKU(sku);
                    break;
                case 4:
                    sc.nextLine(); // consume newline
                    System.out.print("Enter Name to search: ");
                    String name = sc.nextLine();
                    searchByName(name);
                    break;
                case 5:
                    System.out.print("Enter SKU to delete: ");
                    String delSku = sc.next();
                    deleteProduct(delSku);
                    break;
                case 6:
                    System.out.println("Exiting... Thank you!");
                    break;
                default:
                    System.out.println("Invalid choice, try again.");
            }
        } while (choice != 6);
    }
}
