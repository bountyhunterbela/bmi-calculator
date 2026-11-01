print(f"{"="*100}\n{'PERSONAL EXPENSE TRACKER':^60}\n{"="*100}")
expense_name=[]
amount_spent=[]
expense_catagory=[]
while 0<1:
    print(f"{1}.Add an expense")
    print(f"{2}.Display all expenses")
    print(f"{3}.Calculate total expenses")
    print(f"{4}.Find the highest and lowest expenses")
    print(f"{5}.Exit")
    print("="*100)
    choice=int(input("How do you wnat to track your expense today,put your option from the above,please:"))
    if 1<= choice<=5:
        if choice==1:
            name=str(input("Enter your expense name:")).strip().capitalize()
            amount=float(input("Enter your expense amount in birr:"))
            category=str(input("Enter our expense category like food, transportation..:")).strip().capitalize()
            expense_name.append(name)
            amount_spent.append(amount)
            expense_catagory.append(category)
        elif choice==2:
            if len(amount_spent)==0:
                print(f"You got no expense yet,thank you!")
            else:
                print(f"{"="*100}\n{'EXPENSE RECORDES':^60}\n{"="*100}")
                print(f"{'No.':<15}"
                      f"{'Expenses':<40}"
                      f"{'Amount in birr':<25}"
                      f"{'Category':<40}"
                      )
                print("-"*100)
                for index,(ex_na,ex_am,ex_cat) in enumerate(zip(expense_name,amount_spent,expense_catagory),start=1):
                    print(f"{index:<15}"
                          f"{ex_na:<40}"
                          f"{round(ex_am,2):<25}"
                          f"{ex_cat:<40}"
                          )
                print("="*100)
        elif choice==3:
            if len(amount_spent)==0:
                print(f"You got no expense yet,thank you!")
            else:    
                total_expense=0
                for i in amount_spent:
                    total_expense+=i
                print(f"Total expenses:{total_expense:.2f}Birr")
        elif choice==4:
            if len(amount_spent)==0:
                print(f"You got no expense yet,thank you!")
            else:
                y,z,c=max(zip(amount_spent,expense_name,expense_catagory))
                x,b,a=min(zip(amount_spent,expense_name,expense_catagory))
                print(f"Highest expense:{c}-{z}-{y:.2f}Birr")
                print(f"Lowest expense:{a}-{b}-{x:.2f}Birr")
        else:
            print("Exiting the program.....Thank you.")
            break  
    else:
        print(f"Your choice is invalid,try again!")     

            
            



        