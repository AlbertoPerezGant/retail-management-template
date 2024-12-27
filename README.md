# Inventory management template

This repository contains a Python-based **Inventory Management System** template, implemented using two classes: **Product** and **Order**. This solution provides a basic structure to manage inventory for small-scale applications or as a foundation for more advanced systems.

**Features**

**•**	 **Product Management** :

**•**	Add new products to the inventory.

**•**	Update existing product details, such as quantity, price, or supplier.

**•**	Delete products from the inventory.

**•**	Store product details like name, category, quantity, price, and supplier in a shared inventory.

**•**	**Order Management** :

**•**	Place orders for products.

**•**	Automatically update inventory stock after an order is placed.

**•**	Track customer information for each order.

**Classes Overview**

**1. Product Class**

Handles all product-related operations, including managing an inventory stored as a class-level variable.

**Methods:**

**•**	add_product(name, category, quantity, price, supplier)
Adds a new product to the inventory with a unique auto-generated product ID.

**•**	update_product(product_id, quantity=None, price=None, supplier=None)
Updates the details of a product by its ID.

**•**	delete_product(product_id)
Removes a product from the inventory.

**2. Order Class**

Manages orders placed for products in the inventory.

**Methods:**

**•**	place_order(product_id, quantity, customer_info=None)
Places an order for a product, deducts the ordered quantity from inventory, and tracks customer details.

**Usage Example**

**File Structure:**

inventory_management.py

**Example Code:**

```python
from inventory_management import Product, Order

# Add products to inventory

Product.add_product(**"Laptop"**, **"Electronics"**, **50**, **1000**, "Supplier A")

Product.add_product("Tablet", "Electronics", 30, 500, "Supplier B")

# Update a product

Product.update_product(1, quantity=45, price=950)

# Delete a product

Product.delete_product(2)

# Create and place an order

order = Order(order_id=1, products=[])

order.place_order(1, 2, customer_info="John Doe")
```

**Output:**

**•**	Products added successfully.

**•**	Product inventory updated.

**•**	Products deleted if necessary.

**•**	Orders placed with the respective product stock updated.
**Requirements**

**•**	Python 3.6 or later.
**How to Use**

**1.**	Clone the repository.

**2.**	Include your business logic in the **inventory_management.py** file as needed.

**3.**	Extend or modify the classes to suit your specific requirements.
**Notes**

**•**	This template is designed for educational purposes or as a starting point for building a complete inventory management solution.

**•**	Error handling for edge cases (e.g., insufficient stock) is included in the order logic.

Feel free to extend or modify the template to fit your needs! 😊
