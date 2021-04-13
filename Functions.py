import random

database = {}


finalBal = 0
currentBal = 1000 + finalBal


def init():

    print("Welcome to ZuriBank")

    userValidation = int(input("""Are you a registered customer? 
    1. (Yes)
    2. (No)
    """))

    if(userValidation == 1):

        signIn()
    elif(userValidation == 2):

        signUp()
    else:
        print("You have entered an invalid option.")
        init()


def signIn():

    print("Sign in to your ZuriBank account")

    getUserAccountNumber = int(input("Enter your ZuriBank account number \n"))
    userPin = int(input("Enter your 4-digit user PIN: \n"))
    if len(str(userPin)) > 4:
        print("Error! Only 4 numbers is required!")
    for accountNumber, userDetails in database.items():
        if(accountNumber == getUserAccountNumber):
            if(userDetails[3] == userPin):
                bankOperation(userDetails)

    print('Invalid account or PIN')
    init()


def signUp():

    print("Sign Up to Bank with Zuri")

    email = input("Enter your active email address \n")
    first_name = input("Enter your legal first name? \n")
    last_name = input("Enter your last name? \n")
    userPin = int(input("create a 4-digit user PIN for your account \n"))

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name,
                               last_name, email, userPin]

    print("""Congratulations!
    You have registered to bank with Zuri.
     Your account number is: %d""" % accountNumber)
    signIn()


def bankOperation(user):

    print("Welcome %s %s " % (user[0], user[1]))

    bankingOption = int(input(
        "What would you like to do? (1) deposit (2) withdrawal (3) Sign Out (4) Exit \n"))

    if(bankingOption == 1):

        depositRequest()
    elif(bankingOption == 2):

        withdrawalRequest()
    elif(bankingOption == 3):

        SignOut()
    elif(bankingOption == 4):

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)


def withdrawalRequest():

    currentWithdrawal = int(input('How much would you like to withdraw? \n'))
    if currentBal > currentWithdrawal:
        print("""Please take your cash.
        Your Balance is:""")
        finalBal = currentBal - currentWithdrawal
        print(finalBal)
    else:
        print("""Your current balance is lower than %d""" % currentWithdrawal,
              """please make a deposit into your account.""")


def depositRequest():

    currentDeposit = int(input("""" Enter the amount you want to deposit:
    """))
    print("""Your deposit is successful, your current balance is
    """)
    finalBal = currentBal + currentDeposit
    print(finalBal)


def generateAccountNumber():

    return random.randrange(1111111111, 9999999999)


def SignOut():
    signIn()


init()
