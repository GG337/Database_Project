from BANK_MANAGEMENT_SYSTEM import

def main():
    print('''1. Open New Account\n2. Deposit Amount\n3. Withdraw Amount\n4. Balance Enquiry\n5. Dispaly Customer Details\n6. Close An Account''')
    choice =input('Enter The Option You Want: ')
    if (choice =='1'):
        OpenAcc()
    elif(choice =='2'):
        DepoAmo()
    elif(choice =='3'):
        WithdrawAmount()
    elif(choice =='4'):
        BalEnq()
    elif(choice =='5'):
        DisDetails()
    elif(choice =='6'):
        CloseAcc()
    else:
        print('Invalid Choice')
        main()
main()
