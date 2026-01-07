def main():
    products = []
    grand_total = 0

    n = 2

    for i in range(n):
        print(f"\nEnter details for product {i+1}")

        name = laptop
        price = 50000
        quantity = 2

        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)

    print("\n--- Product Summary ---")
    for product in products:
        total = product["price"] * product["quantity"]
        grand_total += total

        print(f"{product['name']}: {product['quantity']} × {product['price']} = {total}")

    print("\nGrand Total Amount:", grand_total)


if __name__ == "__main__":
    main()
