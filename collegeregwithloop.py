print(f"{'='*60}\n{'STUDENT REGISTRATION SYSTEM':^20}\n{'='*60}")
student=[]
age=[]
department=[]
while True:
    print(f"1.Register a student")
    print(f"2.Display registerd students")
    print(f"3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=str(input("Enter your name:")).capitalize()
        ag=int(input("Enter your age:"))
        dep=str(input("Enter your department:")).capitalize()
        student.append(name)
        age.append(ag)
        department.append(dep)
        print(f"Student registerd succesfully!")
    elif choice==2:
        if len(student)==0:
            print(f"No student registerd yet!")
        else:
            print(f"{'='*60}\n{'REGISTERD STUDENTS':^20}\n{'='*60}")
            print(f"{'Registration No.':<18}{'Student':<20}{'Age':<8}{'Department':<25}")
            for index,(students,ages,deps) in enumerate(zip(student,age,department),start=1):
                print(f"{index:<18}{students:<20}{ages:>8}{deps:<25}")
            print('='*60)
    elif choice==3:
        print(f"Exiting the program.....")
        break
    else:
        print(f"Invalid choice!")