import random
import csv

database = {}


def home():

    print("           Welcome to PT Bank")
    print("           *********************")
    return input('1.Create Account\n2.Account Login\nOption : ')

def menu():
    return input('1.Check Balance\n2.Deposit\n3.Withdrawl\nOption : ')

def create_account():
    name = input('Name: ')
    password = input('Password:')
    confirm_Password = input('Confirm Password: ')
    while password != confirm_Password:
        print("Ur password did not match.")
        password = input('Password:')
        confirm_Password = input('Confirm Password: ')
    account_no = random.randrange(100000000, 1000000000)
    while account_no in database:
        account_no = random.randrange(100000000, 1000000000)


    database[account_no]={}
    database[account_no]['name'] = name  
    database[account_no]['password'] = password
    database[account_no]['amount'] = 0
    print('Ur account has been registered.')
    print('Ur account number: ', account_no)
    # print('#############################')

    
status = home()
while status != 'q':
    

    if status == "1":
        create_account()

    elif status == "2":
        user_acc = int(input('Enter ur account number : '))
        if user_acc not in database:
            print("Ur account is nor registered")
            user_option = input('1.Create an account\n2.Exit\nOption : ')
            if user_option == "1":
                create_account()
            

        else:
            password = input('Enter ur password: ')
            while database[user_acc]['password'] != password:
                print("Wrong password!")
                password = input('Enter ur password: ')
        user_option = menu()
        while user_option != '4':
            if user_option == '1':
                print("Balance: ", database[user_acc]["amount"])

            elif user_option == '2':
                deposit_amount = int(input("Enter amount to deposit: "))
                database[user_acc]["amount"] += deposit_amount
                print("Balance: ", database[user_acc]["amount"])   

            elif user_option == '3':
                withdrawl_amount = int(input("Enter amount to withdrawl: "))
                while withdrawl_amount > database[user_acc]["amount"]:
                    print("Ur balance is not insufficient.")
                    print("Balance: ", database[user_acc]["amount"]) 
                    withdrawl_amount = int(input("Enter amount to withdrawl: "))
                database[user_acc]["amount"] -= withdrawl_amount
                print("Balance: ", database[user_acc]["amount"])    
            print('------------------------------')
            user_option = menu()

    else:
        print('Invalid Option! ')

    print('-----------------------------------------')
    status = home() 

print(database)

with open("bank_database.csv","w") as file:
    database_csv = csv.writer(file)
    database_csv.writerow(["Account_No",'Name','Password','Balance'])

    for acc in database:
        database_csv.writerow([acc,database[acc]['name'],database[acc]['password'],database[acc]['amount']])
