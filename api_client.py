import requests


def get_product_by_barcode(barcode):

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        if data["status"] != 1:
            return None

        product = data["product"]

        return {
            "barcode": barcode,
            "product_name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "ingredients": product.get("ingredients_text", "Not Available")
        }

    except Exception:
        return None