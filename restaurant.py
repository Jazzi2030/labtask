menu = {
    1: {"name": "Burger", "price": 500},
    2: {"name": "Pizza", "price": 800},
    3: {"name": "Fries", "price": 250},
    4: {"name": "Drink", "price": 150}
}
def show_menu():
    print("Menu:")
    print("1. Burger Rs. 500")
    print("2. Pizza Rs. 800")
    print("3. Fries Rs. 250")
    print("4. Drink Rs. 150")
def calculate_total(order):
    total = 0
    for item in order:
        total = total + item["price"] * item["quantity"]
    return total
order = []
while True:
    show_menu()
    choice = int(input("Enter item number (0 to finish): "))
    if choice == 0:
        break
    if choice in menu:
        qty = int(input("Enter quantity: "))
        item = {
            "name": menu[choice]["name"],
            "price": menu[choice]["price"],
            "quantity": qty
        }
        order.append(item)
        print(menu[choice]["name"], "added to order")
    else:
        print("Wrong choice, please try again")
    print()
total = calculate_total(order)
print("Final Bill:")
for item in order:
    print(item["name"], "x", item["quantity"],
          "= Rs.", item["price"] * item["quantity"])
print("Total bill: Rs.", total)
file = open("orders.txt", "w")
file.write("Restaurant Order\n\n")
for item in order:
    file.write(item["name"] + " x " + str(item["quantity"])
               + " = Rs. " + str(item["price"] * item["quantity"]) + "\n")
file.write("\nTotal bill: Rs. " + str(total) + "\n")
file.close()
print("Bill saved in orders.txt")
