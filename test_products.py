import subprocess
import sys


def test_products_output():
    # Run the products.py script
    result = subprocess.run(
        [sys.executable, "products.py"],
        capture_output=True,
        text=True
    )

    output = result.stdout

    # Check key outputs
    assert "--- Product Summary ---" in output
    assert "laptop Product: 2 × 50000 = 100000" in output
    assert "Grand Total Amount: 200000" in output
