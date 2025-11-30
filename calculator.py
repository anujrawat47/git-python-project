from utils import add, subtract, multiply, divide

def display_menu():
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", subtract(num1, num2))

        elif choice == '3':
            print("Result:", multiply(num1, num2))

        elif choice == '4':
            try:
                print("Result:", divide(num1, num2))
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
#Menu display function added
# Addition operation implemented
# Subtraction operation added
# Multiplication operation added
# Division operation added
