print("===== ATM MACHINE =====")

balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your Balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance = balance + amount
        print("Money deposited successfully!")
        print("New Balance:", balance)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Please collect your money.")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid Choice!")