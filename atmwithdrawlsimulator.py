user_name=str(input('Account holder:'))
withdrawal_amount=int(input('Withhdrawl:'))
starting_balance=5000
if 0<withdrawal_amount<=starting_balance and withdrawal_amount%100==0:
    status="SUCCES"
    new_balance=starting_balance-withdrawal_amount
    print(f"Transaction :{status:<}")
    print(f"Wtihdrawn   :{withdrawal_amount:<.2f} Birr") 
    print(f"New balance :{new_balance:<.2f} Birr")
else:
    status="Invalid"    
    print(status)