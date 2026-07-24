# Complete this program to classify people by age

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

age = int(input("Enter age: "))
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == "1234":
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        if choice == "1":
            print(f"Your balance {balance}")

        elif choice == "2":
            withdraw  = float(input("Enter your amount withdraw:"))
            balance = balance - withdraw


        elif choice == "3":
            deposit = float(input("Enter your amount deposit: "))
            balance = balance + deposit


        elif choice == "4":
            print(f"End of the Program")
            break
        else:
            print("Invalid PIN")

                    
            

           
        
        # Complete the menu logic here
        # Your code here:

