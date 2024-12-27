from inventory_management import Product, Order

def display_inventory():
    """Helper function to display the inventory in a readable format."""
    print("\nCurrent Inventory:")
    if not Product.inventory:
        print("No products in inventory.")
    else:
        for product in Product.inventory:
            print(f"ID: {product.product_id}, Name: {product.name}, "
                  f"Category: {product.category}, Quantity: {product.quantity}, "
                  f"Price: ${product.price}, Supplier: {product.supplier}")
    print()

def main():
    print("Welcome to the Inventory Management Application\n")

    # Adding products to inventory
    print("Adding products to inventory...")
    Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
    Product.add_product("Tablet", "Electronics", 30, 500, "Supplier B")
    Product.add_product("Smartphone", "Electronics", 100, 700, "Supplier C")
    display_inventory()

    # Updating a product
    print("Updating product ID 1...")
    update_message = Product.update_product(1, quantity=45, price=950)
    print(update_message)
    display_inventory()

    # Deleting a product
    print("Deleting product ID 2...")
    delete_message = Product.delete_product(2)
    print(delete_message)
    display_inventory()

    # Creating and placing an order
    print("Creating and placing an order...")
    order = Order(order_id=1, products=[])
    order_message = order.place_order(1, 2, customer_info="John Doe")
    print(order_message)
    display_inventory()

if __name__ == "__main__":
    main()