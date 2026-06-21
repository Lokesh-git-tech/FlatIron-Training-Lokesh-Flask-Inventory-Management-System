from flask import Flask, jsonify, request

from inventory import (
    get_all_items,
    get_item_by_id,
    add_item,
    update_item,
    delete_item,
    get_next_id
)

from api_client import get_product_by_barcode

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Inventory Management System API"})


# GET all items
@app.route("/inventory", methods=["GET"])
def get_inventory():

    return jsonify(get_all_items()), 200


# GET one item
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):

    item = get_item_by_id(item_id)

    if item:
        return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# POST item
@app.route("/inventory", methods=["POST"])
def create_inventory_item():

    data = request.get_json()

    new_item = {
        "id": get_next_id(),
        "barcode": data.get("barcode"),
        "product_name": data.get("product_name"),
        "brand": data.get("brand"),
        "price": data.get("price"),
        "stock": data.get("stock")
    }

    add_item(new_item)

    return jsonify(new_item), 201


# PATCH item
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def edit_inventory_item(item_id):

    data = request.get_json()

    updated_item = update_item(item_id, data)

    if updated_item:
        return jsonify(updated_item), 200

    return jsonify({"error": "Item not found"}), 404


# DELETE item
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_inventory_item(item_id):

    deleted = delete_item(item_id)

    if deleted:
        return jsonify({"message": "Item deleted successfully"}), 200

    return jsonify({"error": "Item not found"}), 404


# Search OpenFoodFacts by barcode
@app.route("/search-product/<barcode>", methods=["GET"])
def search_product(barcode):

    product = get_product_by_barcode(barcode)

    if product:
        return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)