def main():
    products = []
    grand_total = 0

    n = int(input("Enter number of products: "))

    for i in range(n):
        print(f"\nEnter details for product {i+1}")

        name = input("Product name: ")
        price = float(input("Product price: "))
        quantity = int(input("Product quantity: "))

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
