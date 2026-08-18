products = {
    "Laptop": 80000,
    "Mouse": 2000,
    "Keyboard": 3500,
    "Monitor": 25000
}

def inventory_value(products):

    total = 0

    for product, price in products.items():
        print(product, ":", price)
        total += price

    print("Total Inventory Value:", total)


inventory_value(products)
