card=input('Insert the card: ')
if card=='c':
    print('...Welcome Sowmya...')
    pwd=int(input('Enter the password: '))
    if pwd==1234:
        balance=100000
        while True:
            option=int(input('\t1. Balance Enquiry\n2. Withdrawal\nChoose option: '))
            if option==1:
                print(f"Your account balance is: {balance}")
            elif option==2:
                withdraw=int(input("Enter the amount: "))
                if withdraw<=balance:
                    balance=balance-withdraw
                    print("Please collect your cash")
                    print(f"Remaining account balance is: {balance}")
                else:
                    print("Insufficient balance")
            else:
                print("Invalid option")
    else:
        print('Incorrect password')
else:
    print('Invalid card')
