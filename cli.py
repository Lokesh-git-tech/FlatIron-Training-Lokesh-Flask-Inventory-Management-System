import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():

    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        items = response.json()

        print("\nInventory Items\n")

        for item in items:
            print(
                f"ID: {item['id']} | "
                f"Product: {item['product_name']} | "
                f"Brand: {item['brand']} | "
                f"Price: ${item['price']} | "
                f"Stock: {item['stock']}"
            )

    else:
        print("Failed to retrieve inventory")


def view_single_item():

    item_id = int(input("Enter item ID: "))

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        item = response.json()

        print("\nItem Details")
        print(item)

    else:
        print("Item not found")


def add_inventory_item():

    barcode = input("Barcode: ")
    product_name = input("Product Name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    payload = {
        "barcode": barcode,
        "product_name": product_name,
        "brand": brand,
        "price": price,
        "stock": stock
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=payload
    )

    if response.status_code == 201:
        print("Product added successfully")
    else:
        print("Failed to add product")


def update_inventory_item():

    item_id = int(input("Enter item ID: "))

    price = float(input("New Price: "))
    stock = int(input("New Stock: "))

    payload = {
        "price": price,
        "stock": stock
    }

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=payload
    )

    if response.status_code == 200:
        print("Item updated successfully")
    else:
        print("Item not found")


def delete_inventory_item():

    item_id = int(input("Enter item ID: "))

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    if response.status_code == 200:
        print("Item deleted successfully")
    else:
        print("Item not found")


def search_openfoodfacts():

    barcode = input("Enter barcode: ")

    response = requests.get(
        f"{BASE_URL}/search-product/{barcode}"
    )

    if response.status_code == 200:

        product = response.json()

        print("\nProduct Found")
        print(product)

    else:
        print("Product not found")


def add_product_from_api():

    barcode = input("Enter barcode: ")

    response = requests.get(
        f"{BASE_URL}/search-product/{barcode}"
    )

    if response.status_code != 200:
        print("Product not found")
        return

    product = response.json()

    print("\nProduct Found")
    print(product)

    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))

    payload = {
        "barcode": product["barcode"],
        "product_name": product["product_name"],
        "brand": product["brand"],
        "price": price,
        "stock": stock
    }

    add_response = requests.post(
        f"{BASE_URL}/inventory",
        json=payload
    )

    if add_response.status_code == 201:
        print("Product added to inventory")
    else:
        print("Failed to add product")


def menu():

    while True:

        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. View Single Item")
        print("3. Add Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Search OpenFoodFacts")
        print("7. Add Product From OpenFoodFacts")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_single_item()

        elif choice == "3":
            add_inventory_item()

        elif choice == "4":
            update_inventory_item()

        elif choice == "5":
            delete_inventory_item()

        elif choice == "6":
            search_openfoodfacts()

        elif choice == "7":
            add_product_from_api()

        elif choice == "8":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()