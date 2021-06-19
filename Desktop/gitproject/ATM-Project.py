def welcome_menu():
    print("Welcome to CHIOMA Bank")


def enter_pin(pin, pin1):
    if pin == pin1:
        return True
    else:
        return False


def deposit_money(balance):
    deposit = float(input('How much would you like to deposit?\n'))
    balance = round(balance + deposit, 2)
    print('\nYour account balance is now ', balance)
    continue_use(balance)


def withdraw_money(balance):
    withdrawal = float(input('How much would you like to withdraw?\n'))
    if withdrawal > balance:
        print("You have insufficient funds !")
        continue_use(balance)
    else:
        balance = round(balance - withdrawal, 2)
        print('Your account balance is now ', balance)
        continue_use(balance)


def check_balance(balance):
    print('\nYour account balance is', round(balance, 2))
    continue_use(balance)


def exit_option():
    print('\nPlease take your card.....')
    print("Thank you for banking with us.")


def start_menu(balance):
    print('\nPlease press 1 to view your account Balance')
    print('Please press 2 to make a Withdrawal')
    print('Please press 3 to make deposit')
    print('Please press 4 to exit the machine')

    option = int(input('Which Option will you like to Select? '))

    if option == 1:
        check_balance(balance)
    elif option == 2:
        withdraw_money(balance)
    elif option == 3:
        deposit_money(balance)
    else:
        exit_option()


def continue_use(balance):
    print("\nWill you like to perform another transaction.")
    use = input("Press y/Y to continue or any key quit: ")
    if use == 'y' or use == 'Y':
        start_menu(balance)


def contact_us():
    print("Please contact us to issue a new PIN.")


def main():
    trials = 0
    pin = 1234
    balance = 40.12

    welcome_menu()

    while True:
        if trials < 3:
            pin1 = int(input("Enter your 4 digit pin: "))
            if enter_pin(pin, pin1):
                start_menu(balance)
                break
            else:
                trials = trials + 1
                print("Invalid Pin, please try again\n")
        else:
            print("You have exceeded your pin trials")
            contact_us()
            break


if __name__ == "__main__":
    main()
