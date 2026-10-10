def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def modulus(a, b):
    return a % b
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    choice = input("Enter your choice: ")
    if choice == "1" or choice == "+":
        print("Result:", add(num1, num2))
    elif choice == "2" or choice == "-":
        print("Result:", subtract(num1, num2))
    elif choice == "3" or choice == "*":
        print("Result:", multiply(num1, num2))
    elif choice == "4" or choice == "/":
        if num2 != 0:
            print("Result:", divide(num1, num2))
        else:
            print("Cannot divide by zero")
    elif choice == "5" or choice == "%":
        print("Result:", modulus(num1, num2))
    else:
        print("Wrong choice")
    again = input("Do you want to do another calculation? (yes/no): ")
    if again == "no":
        print("Calculator closed")
        break
