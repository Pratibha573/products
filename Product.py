def get_product_details(product_id, name, quantity, price):
    """
    This function accepts product details and returns
    a well-formatted string containing all the provided information.
    """
    return (
        f"--- Product Details ---\n"
        f"Product ID : {product_id}\n"
        f"Name       : {name}\n"
        f"Quantity   : {quantity}\n"
        f"Price      : {price}"
    )

# Example usage (optional for demonstration)
if __name__ == "__main__":
    print(get_product_details("P101", "Laptop", 2, 55000))