import json
from operator import add
print("********************************")
print("WELL-COME to the ATM Machine ")
print("********************************")


with open("customers.json", "r") as file:
    customers = json.load(file)
def save_data():
    with open("customers.json", "w") as file:
        json.dump(customers, file, indent=4)

username=input("Enter your user name: ")
entered_pin=int(input("Enter your password: "))
if username in customers and customers[username]["Password"]==entered_pin:
    print(f"Well-Come: {username}",customers[username])

    def change_pin():
            
            old_pin=int(input("Enter your past pin first: "))
            if old_pin == customers[username]["Password"]:
                new_pin=int(input("Enter new pin: "))
                customers[username]["Password"]=new_pin
                save_data()
                print("PIN changed successfully")
            else:
                print("please enter correct pin..")
                
    def check_balance():
            pin=int(input("Enter your pin to check (Balance): "))
            if pin==customers[username]["Password"]:
                print("Your balance is :",customers[username]["balance"])
                save_data()
            else:
                print("Please enter correct pin..")
            
    def withdraw():
            
            user_pin=int(input("Enter your pin :  "))
            if user_pin == customers[username]["Password"]:
              money=int(input("Enter amount to withdraw: "))
              if money <= customers[username]["balance"]:
                customers[username]["balance"] -=money
                print("Withdraw successufly.......")
                print("Remaining balance: ",customers[username]["balance"])
                save_data()
              else:
                        print("Inflluence balance ")
            else:
                print("Please Enter corect pin...")


    def deposit():
            Money=int(input("Enter amount to deposit: "))
            if Money > 0 :
                customers[username]["balance"]+=Money
                print("Deposited money ",(Money))
                print("Updated balance ",customers[username]["balance"])
                save_data()
            else:
                print("Please enter right balance..")
    def Address():
        user_ip=int(input("Enter your password: "))
        if user_ip == customers[username]["Password"]:
            add=input("Enter new address: ")
            customers[username]["Address"]=add
            print("New address is : ",customers[username]["Address"])
            save_data()
        else:
            print("Please enter correct pin: ")
      

    while True:
            print("\n******** MENU ********")
            print("(1).Balance "),
            print("(2).Withdrw "),
            print("(3).Deposit "),
            print("(4).Change pin"),
            print("(5).Change Address ")
            print("(6).Exit ")
            print("-------------------------")

            options=int(input("Please select an option between 1.....5 :\n-> "))
            if options == 1:
                check_balance()
            elif options == 2:
                withdraw()
            elif options == 3:
                deposit()
            elif options == 4:
                change_pin()
            elif options== 5:
                Address()
            elif options == 6:
                print("Thank you! ")
                break
            else:
                print("Please select correct pin..")
    else:
        print("Plese enter correect acount name and password! ")
        
