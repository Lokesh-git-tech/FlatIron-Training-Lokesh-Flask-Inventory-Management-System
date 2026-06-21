import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from unittest.mock import patch
from api_client import get_product_by_barcode


@patch("api_client.requests.get")
def test_get_product_by_barcode_success(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Nutella",
            "brands": "Ferrero",
            "ingredients_text": "Sugar, Palm Oil"
        }
    }

    product = get_product_by_barcode("3017620422003")

    assert product["product_name"] == "Nutella"
    assert product["brand"] == "Ferrero"


@patch("api_client.requests.get")
def test_get_product_by_barcode_not_found(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "status": 0
    }

    product = get_product_by_barcode("999999")

    assert product is None


@patch("api_client.requests.get")
def test_get_product_by_barcode_api_failure(mock_get):

    mock_get.side_effect = Exception("API Error")

    product = get_product_by_barcode("123")

    assert product is None