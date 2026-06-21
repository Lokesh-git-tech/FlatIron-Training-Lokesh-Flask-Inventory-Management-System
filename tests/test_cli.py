import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from unittest.mock import patch
import cli


@patch("builtins.print")
@patch("cli.requests.get")
def test_view_inventory(mock_get, mock_print):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = [
        {
            "id": 1,
            "product_name": "Milk",
            "brand": "Brand A",
            "price": 4.99,
            "stock": 20
        }
    ]

    cli.view_inventory()

    assert mock_get.called


@patch("builtins.input", side_effect=[
    "12345",
    "Protein Bar",
    "MyBrand",
    "3.99",
    "50"
])
@patch("cli.requests.post")
def test_add_inventory_item(mock_post, mock_input):

    mock_post.return_value.status_code = 201

    cli.add_inventory_item()

    assert mock_post.called


@patch("builtins.input", side_effect=[
    "1",
    "9.99",
    "100"
])
@patch("cli.requests.patch")
def test_update_inventory_item(mock_patch, mock_input):

    mock_patch.return_value.status_code = 200

    cli.update_inventory_item()

    assert mock_patch.called


@patch("builtins.input", side_effect=["1"])
@patch("cli.requests.delete")
def test_delete_inventory_item(mock_delete, mock_input):

    mock_delete.return_value.status_code = 200

    cli.delete_inventory_item()

    assert mock_delete.called


@patch("builtins.input", side_effect=["3017620422003"])
@patch("cli.requests.get")
def test_search_openfoodfacts(mock_get, mock_input):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "barcode": "3017620422003",
        "product_name": "Nutella",
        "brand": "Ferrero"
    }

    cli.search_openfoodfacts()

    assert mock_get.called