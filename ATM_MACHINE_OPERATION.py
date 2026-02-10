balance = 5000.0
PIN = "6541"

user_pin = input("Enter your 4-digit PIN: ")
while user_pin != PIN:
    print("Incorrect PIN! Try again.")
    user_pin = input("Enter your 4-digit PIN: ")

while True:
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: Rs. {balance:.2f}")
    
    elif choice == '2':
        amount = input("Enter deposit amount: Rs. ")
        while not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
            print("Invalid amount! Must be a positive number.")
            amount = input("Enter deposit amount: Rs. ")
        amount = float(amount)
        balance += amount
        print(f"Rs. {amount:.2f} deposited successfully!")
    
    elif choice == '3':
        amount = input("Enter withdrawal amount: Rs. ")
        while not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
            print("Invalid amount! Must be a positive number.")
            amount = input("Enter withdrawal amount: Rs. ")
        amount = float(amount)
        if amount <= balance:
            balance -= amount
            print(f"Please collect your cash: Rs. {amount:.2f}")
        else:
            print("Insufficient balance!")
    
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select 1-4.")
