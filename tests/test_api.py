import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True

    with app.test_client() as client:
        yield client


def test_get_all_inventory(client):

    response = client.get("/inventory")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)


def test_get_single_inventory_item(client):

    response = client.get("/inventory/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1


def test_get_invalid_inventory_item(client):

    response = client.get("/inventory/999")

    assert response.status_code == 404


def test_create_inventory_item(client):

    payload = {
        "barcode": "123456",
        "product_name": "Protein Bar",
        "brand": "Test Brand",
        "price": 3.99,
        "stock": 50
    }

    response = client.post(
        "/inventory",
        json=payload
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["product_name"] == "Protein Bar"


def test_update_inventory_item(client):

    payload = {
        "price": 9.99,
        "stock": 100
    }

    response = client.patch(
        "/inventory/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["price"] == 9.99
    assert data["stock"] == 100


def test_update_invalid_inventory_item(client):

    payload = {
        "price": 9.99
    }

    response = client.patch(
        "/inventory/999",
        json=payload
    )

    assert response.status_code == 404


def test_delete_inventory_item(client):

    response = client.delete("/inventory/2")

    assert response.status_code == 200


def test_delete_invalid_inventory_item(client):

    response = client.delete("/inventory/999")

    assert response.status_code == 404


def test_search_product_route_exists(client):

    response = client.get(
        "/search-product/3017620422003"
    )

    assert response.status_code in [200, 404]