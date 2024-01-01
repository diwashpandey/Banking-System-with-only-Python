# This is the basic banking system with just Python
# No External Modules/Frameworks have been used

import datetime
import os
import sys
import time

DATABASE_PATH = "Accounts_Database"

class History_Database:

    @classmethod
    def add_history(cls, acc_no, record):
        with open(f"{DATABASE_PATH}/{acc_no}/{acc_no}-History.txt", "a") as file:
            file.write(f"{record}\n")

    def get_history(self, acc_no):
        with open(f"{DATABASE_PATH}/{acc_no}/{acc_no}-History.txt", "r") as file:
            details = file.read()
        print(details)


class Accounts_Database:
    def add_acc(self, name, pin, balance=0):
        print("Creating your account...")
        fake_load()
        if not os.path.exists(DATABASE_PATH):
            os.makedirs(f"{DATABASE_PATH}")

        acc_no = 100000 + len(os.listdir(f"{DATABASE_PATH}/"))
        os.makedirs(f"{DATABASE_PATH}/{acc_no}")

        assemble(acc_no, name, pin, balance)

        with open(f"{DATABASE_PATH}/{acc_no}/{acc_no}-History.txt", "a"):
            pass  # Just to create the file

        print(f"Your account number is {acc_no}. Please note it down.")

        record = f"{get_time()} Created a new account"
        History_Database.add_history(acc_no, record)
        wait()

    def close_acc(self, acc_no):
        acc_no, name, pin, balance, active = deassemble(acc_no)
        print("Deleting account...")
        fake_load()

        assemble(acc_no, name, pin, balance, active=False)

        record = f"{get_time()} Account Closed!"
        History_Database.add_history(acc_no, record)


class Security:
    def acc_exist(self, acc_num, given_name=""):
        clr_screen()
        print("Searching for account...")
        fake_load()

        if os.path.exists(f"{DATABASE_PATH}/{acc_num}"):
            acc_num, name, pin, balance, active = deassemble(acc_num)
            if active == "True" and name == name:
                print("Account Found✅...")
                wait()
                return True

            elif active == "False":
                print("This account was Deleted❕")
                wait()
                return False

        else:
            print("Sorry!!! Account not found...❌")
            wait()
            return False

    def correct_pin(self, acc_no, given_pin):
        acc_no, name, pin, balance, active = deassemble(acc_no)
        clr_screen()
        print("Checking PIN...")
        fake_load()
        if given_pin == pin:
            print("PIN Matched...✅")
            return True
        else:
            print("PIN did not match❌")
            wait()
            return False


class System(History_Database, Accounts_Database, Security):
    def withdraw(self, acc_no, given_amount):
        acc_no, name, pin, balance, active = deassemble(acc_no)
        print("Withdraw in process... Please wait...")
        fake_load()
        check_balance(given_amount, balance)
        if check_balance:
            print("Transaction Unsuccessful.❌ You don't have enough balance!!!")
            wait()
        else:
            new_balance = balance - given_amount
            assemble(acc_no, name, pin, balance=new_balance)
            record = f"{get_time()} withdraw rs{given_amount}"
            History_Database.add_history(acc_no, record)
            print("Transaction Successful...✅")
            print(f"rs{given_amount} successfully withdraw from the account!!!")
            print(f"Your new balance is: {new_balance}")
            wait()

    def deposit(self, acc_no, given_amount):
        acc_no, name, pin, balance, active = deassemble(acc_no)
        print("Transaction in process... Please wait...")
        fake_load()

        new_balance = given_amount + balance

        assemble(acc_no, name, pin, new_balance)

        record = f"{get_time()} Deposited Rs,{given_amount}"
        History_Database.add_history(acc_no, record)
        print("Transaction Successful...✅")
        print(f"rs{given_amount} deposited into account..")
        print(f"Your new balance is: {new_balance}")
        wait()

    def transfer(self, from_acc, to_acc, given_amount):
        print("Transaction in process... Please wait...")
        fake_load()

        from_acc_no, name, pin, balance, active = deassemble(from_acc)

        if check_balance(given_amount, balance):
            print("Passed balance check")  # Temporary code
            new_declared_balance = balance - given_amount
            assemble(from_acc_no, name, pin, new_declared_balance)
            print("balance demised from account check")  # Temporary code
            #Balance has been demised from the account

            #now opening new account
            to_acc_no, name, pin, balance, active = deassemble(to_acc)
            new_increased_balance = balance + given_amount

            assemble(to_acc_no, name, pin, new_increased_balance)

            # History record for sender_account
            transfered_record = f"{get_time()} Transfered rs,{given_amount} to account no.{to_acc}"
            History_Database.add_history(from_acc, transfered_record)

            # History record for receiver
            record = f"{get_time()} Received rs,{given_amount} from account no.{from_acc}"
            History_Database.add_history(to_acc, record)

            print(f"rs,{given_amount} transfered successfully to {to_acc}✅")
            print(f"Your new balance is: {new_declared_balance}")
            wait()

        else:
            print("Sorry, you don't have enough balance to transfer!❌")
            wait()
            welcome()

    def show_detail(self, acc_no):
        acc_no, name, pin, balance, active = deassemble(acc_no)
        print("Getting information...")
        fake_load()
        print(f"Account number:{acc_no}\n"
              f"Name: {name}\n"
              f"Balance = {balance}")
        wait()


def welcome():
    clr_screen()
    global run, user_choice
    print(r'''
     __       __          __                                         
    |  \  _  |  \        |  \                                        
    | $$ / \ | $$ ______ | $$ _______  ______  ______ ____   ______  
    | $$/  $\| $$/      \| $$/       \/      \|      \    \ /      \ 
    | $$  $$$\ $|  $$$$$$| $|  $$$$$$|  $$$$$$| $$$$$$\$$$$|  $$$$$$\
    | $$ $$\$$\$| $$    $| $| $$     | $$  | $| $$ | $$ | $| $$    $$
    | $$$$  \$$$| $$$$$$$| $| $$_____| $$__/ $| $$ | $$ | $| $$$$$$$$
    | $$$    \$$$\$$     | $$\$$     \\$$    $| $$ | $$ | $$\$$     \
     \$$      \$$ \$$$$$$$\$$ \$$$$$$$ \$$$$$$ \$$  \$$  \$$ \$$$$$$$


    ''')
    print("This is Banking system by Diwash🤑💵")
    print("Press:"
          "\n1.Deposit Cash"
          "\n2.Withdraw Cash"
          "\n3.Create an Account"
          "\n4.Show Bank Details"
          "\n5.Close Account"
          "\n6.Transfer Money"
          "\n7.To exit")
    try:
        user_choice = int(input("\nWhat do you want to proceed with?\n:"))
    except:
        error()

    clr_screen()

    match user_choice:
        case 1:
            print("\nYou chose deposit money...\n")
            acc_num = int(input("Please enter the account number you want to deposit to:"))
            name = input("Please enter the account name:")

            if system.acc_exist(acc_num, name):
                amount = int(input("Please enter the amount you want to deposit:"))
                clr_screen()
                system.deposit(acc_num, amount)
            else:
                clr_screen()

        case 2:
            print("\nYou chose Withdraw cash...\n")
            acc_no = int(input("Please enter your account number:"))
            name = input("Please enter the account name:")

            if system.acc_exist(acc_no, name):
                pin = int(input("Please enter your PIN:"))
                if system.correct_pin(acc_no, pin):
                    amount = int(input("Please enter the amount you want to withdraw:"))
                    system.withdraw(acc_no, amount)

            else:
                clr_screen()

        case 3:
            print("\nYou chose add an account...\n")
            new_name = input("Please enter your full name:")
            new_pin = int(input("Please enter your PIN:"))
            pin_confirmation = int(input("Please verify your PIN:"))
            clr_screen()
            if not len(str(new_pin)) == 4:
                print("Error!!! PIN should be in 4 digits")
                wait()
            if new_pin == pin_confirmation:
                system.add_acc(new_name, new_pin)
            else:
                print("Your PIN did not match,\nPlease try again")
                wait()

        case 4:
            print("\nYou chose show detail...\n")
            acc_no = int(input("Please enter your account number:"))
            name = input("Please enter account name:")

            if system.acc_exist(acc_no, name):
                pin = int(input("Please enter your PIN:"))
                if system.correct_pin(acc_no, pin):
                    system.show_detail(acc_no)

        case 5:
            print("\nYou chose close account...")
            acc_no = int(input("Please enter the account no. that you want to delete:"))
            name = input("Please enter your account name:")
            if system.acc_exist(acc_no, name):
                pin = int(input("Please enter your PIN:"))
                if system.correct_pin(acc_no, pin):
                    wait()
                    system.close_acc(acc_no)
        case 6:
            print("\nYou chose transfer money...")
            from_acc = int(input("Please enter the account no. your account no.:"))
            
            if system.acc_exist(from_acc):
                to_acc = int(input("Please enter the account no. you want to send money:"))

                if from_acc == to_acc:
                    print("Sorry, you cannot transfer to the same account❌")
                    wait()
                else:
                    if system.acc_exist(to_acc):
                        pin = int(input("Please enter your PIN:"))
                        if system.correct_pin(from_acc, pin):
                            amount = int(input("Please enter the amount you want to send:"))
                            system.transfer(from_acc, to_acc, amount)

        case 7:
            clr_screen()
            run = False


def deassemble(acc_no):
    with open(f"{DATABASE_PATH}/{acc_no}/{acc_no}-Details.txt", "r") as file:
        line = file.readline()
        parts = line.strip().split(':')

        return int(parts[0]), parts[1], int(parts[2]), int(parts[3]), parts[4]


def get_time():
    time = datetime.datetime.today()
    return time.strftime("%A, %d %B, %Y at %I:%M:%S %p->")


def assemble(acc_no, name, pin, balance, active=True):
    with open(f"{DATABASE_PATH}/{acc_no}/{acc_no}-Details.txt", "w") as file:
        file.write(details_format(acc_no, name, pin, balance, active))
    clr_screen()


def check_balance(given_amount, balance):
    if given_amount > balance:
        return False
    elif given_amount <= balance:
        return True
    else:
        raise ValueError("Value error while checking balance")


def details_format(acc_no, name, pin, balance, active=True):
    return f"{acc_no}:{name}:{pin}:{balance}:{active}\n"


def clr_screen():
    os.system("cls")


def wait():
    input("\nPress enter to continue...")
    clr_screen()


def fake_load():
    print("⌛", end="", flush=True)
    time.sleep(1)
    print("⌛", end="", flush=True)
    time.sleep(1)
    print("⌛", end="", flush=True)
    time.sleep(1)
    print("⏳", end="", flush=True)
    clr_screen()


def error():
    print("🚫!!!!Some Error Occurred!!!!🚫")
    print("Please give proper input if you are not")
    input("\n\nPress enter to restart...")


global user_choice, run
run = True

if __name__ == "__main__":
    if sys.platform == 'win32':
        os.system('chcp 65001')
        clr_screen()

    system = System()
    try:
        while run:
            welcome()
    except:
        clr_screen()
        error()
        welcome()
