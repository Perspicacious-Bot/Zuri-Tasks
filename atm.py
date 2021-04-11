import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

username = input("Enter Your Username: \n")

regUsers = ["CodePoet", "Frank", "Bishop", "Adeboye"]

usersPass = ["1234", "Gent45", "eL9", "7806"]

if (username in regUsers):
    password = input("Enter Your Password: \n")
    userId = regUsers.index(username)

    if (password == usersPass[userId]):

        print('Welcome %s' % username)
        print('These are the available options.')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        userOption = int(input('Please select an option number \n'))

        if (userOption == 1):
            optionOne = int(input('How much would you like to withdraw? \n'))
            print('Please take your cash')

        elif (userOption == 2):
            initialBal = 1600
            userDeposit = int(input('How much would you like to deposit? \n'))
            currentBal = initialBal + userDeposit
            print('Your cash deposit is successful')
            print('Your current balance is %s' % currentBal)

        elif (userOption == 3):
            input('What issue will you like to report? \n')
            print('Thank you for contacting us')

        else:
            print('Invalid Option selected, please try again.')

    else:
        print("Invalid Password.")

else:
    print('The Username %s' % username + ' is invalid')
