from products import product_details


def test_products_output():
    output = product_details()

    assert "--- Product Summary ---" in output
    assert "laptop Product: 2 × 50000 = 100000" in output
    assert "Grand Total Amount: 200000" in output
