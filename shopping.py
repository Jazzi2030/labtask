def calculate_bill(products):
    total = 0
    for p in products:
        total = total + p["total_price"]
    return total
products = []
for i in range(5):
    print("Enter details of product", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    total_price = price * quantity
    product = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total_price": total_price
    }
    products.append(product)
    print()
bill = calculate_bill(products)
discount = 0
if bill > 10000:
    discount = bill * 10 / 100
final_bill = bill - discount
print("Final Bill:")
for p in products:
    print(p["name"], "- Price:", p["price"],
          "- Quantity:", p["quantity"],
          "- Total:", p["total_price"])
print("Total bill:", bill)
print("Discount:", discount)
print("Bill after discount:", final_bill)
costly = products[0]
for p in products:
    if p["total_price"] > costly["total_price"]:
        costly = p
print("Most expensive product:", costly["name"])
file = open("bill.txt", "w")
file.write("Shopping Bill\n\n")
for p in products:
    file.write(p["name"] + " - Price: " + str(p["price"])
               + ", Quantity: " + str(p["quantity"])
               + ", Total: " + str(p["total_price"]) + "\n")
file.write("\nTotal bill: " + str(bill) + "\n")
file.write("Discount: " + str(discount) + "\n")
file.write("Bill after discount: " + str(final_bill) + "\n")
file.close()
print("Bill saved in bill.txt")
