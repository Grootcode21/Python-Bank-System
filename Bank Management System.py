import os.path as o
import pickle as p
import random as r


def get_all_accounts():
    if o.isfile("Account.bat"):
        read_file = open("Account.bat", "rb")
        accounts = p.load(read_file)
        read_file.close()
        return accounts
    else:
        return {}


def write_accounts(accounts):
    write_file = open("Account.bat", "wb")
    p.dump(accounts, write_file)
    write_file.close()


def display_account(act):
    accounts = get_all_accounts()
    print("-" * 80)
    print("Holder's Name: ", act[0])
    print("Phone: ", act[1])
    print("Address: ", act[2])
    print("Gender: ", act[3])
    print("Password: ", act[4])
    print("Balance: ", act[5])


def add_account():
    accounts = get_all_accounts()
    ac_no = input("Enter Account Number: ")
    if ac_no in accounts.keys():
        print("This account number already exists")
        return

    name = input("Enter Account holder name: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    gender = input("Enter gender: ")
    password = r.randint(100000, 1000000)
    balance = 0

    accounts[ac_no] = [name, phone, address, gender, password, balance]

    write_accounts(accounts)
    print("Account has been created successfully...")


def remove_account():
    accounts = get_all_accounts()
    ac_no = input("Enter Account Number: ")
    if ac_no in accounts.keys():
        del accounts[ac_no]
        print("Account has been Deleted Successfully!")
        write_accounts(accounts)
    else:
        print("Account Does not exist")


def edit_account():
    accounts = get_all_accounts()
    ac_no = input("Enter Account Number: ")
    if ac_no in accounts.keys():
        display_account(accounts[ac_no])
        print("What do you want to change?")
        print("0.Holder's name: ")
        print("1.Phone: ")
        print("2.Address: ")
        print("3.Gender: ")
        choice = int(input())
        if choice <= 0 and choice < 4:
            v = input("Enter New Value: ")
            if v != "":
                accounts[ac_no][choice] = v
                print("Account has been Updated Successfully")
                write_accounts(accounts)
            else:
                print("Please Try Again")
        else:
            print("Wrong Choice!")
    else:
        print("Account Does not exist")


def display_all_accounts():
    accounts = get_all_accounts()
    print("-" * 80)
    print("Account Table".center(80))
    print("-" * 80)
    for account in accounts:
        print(account, accounts[account])


def search_accounts():
    accounts = get_all_accounts()
    ac_no = input("Enter Account Number: ")
    if ac_no in accounts.keys():
        display_account(accounts[ac_no])
    else:
        print("Account does not exist")


def admin_menu():
    print("-" * 80)
    print("Groot Banking System".center(80))
    print("-" * 80)
    print("1.Add New Account")
    print("2.Remove Account")
    print("3.Edit Account")
    print("4.Display All Accounts")
    print("5.Search Accounts")
    print("0.Exit")

    choice = int(input("Select.."))
    if choice == 1:
        add_account()
    elif choice == 2:
        remove_account()
    elif choice == 3:
        edit_account()
    elif choice == 4:
        display_all_accounts()
    elif choice == 5:
        search_accounts()
    elif choice == 0:
        exit()

    input("Continue...")
    admin_menu()


def deposit_cash(ac_no):
    accounts = get_all_accounts()
    amount = int(input("Enter the amount to Deposit: "))
    accounts[ac_no][5] = int(accounts[ac_no][5] + amount)
    write_accounts(accounts)
    print("Amount Deposited Successfully")


def withdraw_cash(ac_no):
    accounts = get_all_accounts()
    amount = int(input("Enter Amount to Withdraw: "))
    if accounts[ac_no][5] > amount:
        accounts[ac_no][5] = int(accounts[ac_no][5]) - amount
        write_accounts(accounts)
        print("Amount withdrawn Successfully")
    else:
        print("You cannot withdraw. Your Balance is: ", accounts[ac_no][5])


def check_balance(ac_no):
    accounts = get_all_accounts()
    print("Balance is Kshs ", accounts[ac_no][5])


def account_details(ac_no):
    accounts = get_all_accounts()
    display_account(accounts[ac_no])


def customer_menu(ac_no):
    print("-" * 80)
    print("Customer Panel".center(80))
    print("-" * 80)
    print("1.Deposit Cash")
    print("2.Withdraw Cash")
    print("3.Check Balance")
    print("4.Account Details")
    print("0.Exit")

    choice = int(input("Select.."))
    if choice == 1:
        deposit_cash(ac_no)
    elif choice == 2:
        withdraw_cash(ac_no)
    elif choice == 3:
        check_balance(ac_no)
    elif choice == 4:
        account_details(ac_no)
    elif choice == 0:
        exit()

    input("Continue...")
    customer_menu(ac_no)


def main_menu():
    print("-" * 80)
    print("Groot Banking System".center(80))
    print("-" * 80)
    print("1.Admin Login\n2.Customer Login")
    choice = int(input("Select: "))
    if choice == 1:
        admin_id = input("Enter Admin ID: ")
        password = input("Enter Admin Password: ")
        if admin_id == "Grootcode21" and password == "inferni":
            admin_menu()
        else:
            print("ID/Password is not matched...")
    elif choice == 2:
        accounts = get_all_accounts()
        ac_no = input("Enter Account Number: ")
        if ac_no in accounts.keys():
            password = int(input("Enter Password: "))
            if accounts[ac_no][4] == password:
                customer_menu(ac_no)
            else:
                print("Password does not match")
        else:
            print("Account Not Available")
