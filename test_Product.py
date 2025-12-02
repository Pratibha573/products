# test_product.py

from product import get_product_details

def test_get_product_details():
    # Sample input data
    product_id = "P202"
    name = "Mobile Phone"
    quantity = 3
    price = 15000

    # Expected formatted output
    expected_output = (
        "--- Product Details ---\n"
        "Product ID : P202\n"
        "Name       : Mobile Phone\n"
        "Quantity   : 3\n"
        "Price      : 15000"
    )

    # Assertion to verify the function output
    assert get_product_details(product_id, name, quantity, price) == expected_output