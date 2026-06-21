# Simulated inventory database

inventory = [
    {
        "id": 1,
        "barcode": "737628064502",
        "product_name": "Organic Almond Milk",
        "brand": "Silk",
        "price": 4.99,
        "stock": 20
    },
    {
        "id": 2,
        "barcode": "3017620422003",
        "product_name": "Nutella",
        "brand": "Ferrero",
        "price": 6.99,
        "stock": 15
    }
]


def get_all_items():
    return inventory


def get_item_by_id(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item

    return None


def add_item(item):
    inventory.append(item)


def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return True

    return False


def update_item(item_id, updated_data):
    item = get_item_by_id(item_id)

    if item:
        item.update(updated_data)
        return item

    return None


def get_next_id():
    if len(inventory) == 0:
        return 1

    return max(item["id"] for item in inventory) + 1