#stage 1
students=["Abel","Hana","Dawit","Sara","Samuel"]
print(f"{'_'*100}\n{"="*100}\n==\n{"STUDENT REGISTRATION":^20}\n{"="*100}\n==")
print(f"Registered Students:\n{students}")
print(f"First Student:  {students[0]}")
print(f"Second Student: {students[1]}")
print(f"First Three Students:\n{students[0:3]}")
print(f"Total Students: {len(students)} ")
print(f"Is Sara Registerd?  :{"Sara" in students}")
print(f"{"-"*100}\n{'UPDATED REGISTRATION':^20}\n{'-'*100}")
students.append("Mekdes")
print(f"After Adding Mekdes:\n{students}")
students.remove("Hana")
print(f"After Removing Hana:\n{students}")
students[2]="Dawit Bekele"
print(f"After Updating Dawit:\n{students}")
print(f"{'='*100}\n==")
#stage 2
college_infos=("ABC College","Addis Ababa",1998,"ABC-01")
print(f"{"_"*100}\n{"="*100}\n==\n{"COLLEGE INFORMATION":^}\n{"="*100}\n==")
print(f"College Information:\n{college_infos}")
print(f"College Name: {college_infos[0]}")
print(f"Establishment Year:{college_infos[2]}")
print(f"First Two Elements:\n{college_infos[:2]}")
print(f"Is Addis Ababa Available?   {"Addis Ababa" in college_infos}")
print(f"Total Information Items: {len(college_infos)}")
print(f"{"="*100}\n==")
# college information is stored in tuple rather than list because college information can't be added or removed or created or generally immutable like tuples.
# stage 3
python_programming={"Abel","Hana","Sara","Samuel"}
mathematics={"Abel","Dawit","Sara"}
computer_engineering={"Hana","Dawit","Samuel"}
print(f"{"_"*100}\n{"="*100}\n==\n{"COURSE ENROLLMENT SYSTEM":^}\n{"="*100}\n==")
print(f"Python Students:\n{python_programming}")
print(f"Mathematics Students:\n{mathematics}")
print(f"Computer Enginering Students:\n{computer_engineering}")
print(f"{"-"*100}\n{'COURSE COMPARISON':^20}\n{'-'*100}")
print(f"Python AND Mathematics:\n{python_programming&mathematics}")
print(f"Python  BUT NOT Mathematics:\n{python_programming-mathematics}")
print(f"Mathematics BUT NOT Python:\n{mathematics-python_programming}")
print(f"Exactly One Course:\n{mathematics^python_programming}")
print(f"All Registered Students:\n{mathematics|computer_engineering|python_programming}")
print(f"Students in All Three Courses:\n{mathematics&computer_engineering&python_programming}")
print(f"Total Unique Students:{len(python_programming|mathematics|computer_engineering)}")
print(f"IS Abel In Python? :{"Abel" in python_programming}")
print(f"Is Mekdes In Mathematics? :{"Mekdes"in mathematics} ")
print(f"{"="*100}\n==")
#stag 4
ass=(80,65,45,90,55)
mid=(75,70,50,85,60)
fin=(90,80,55,95,65)
print(f"{"_"*100}\n{"="*100}\n==\n{"EXAMINATION RESULT SYSTEM":^}\n{"="*100}\n==")
T=(ass[0]*0.2)+(mid[0]*0.3)+(fin[0]*0.5)
if 0<=T<= 100:
    if 90<=T<=100:
        grade="A⁺"
        stat="PASS"
    elif 80<=T <=89.99:
        grade="A"
        stat="PASS"
    elif 70<=T<=79.99:
        grade="B"
        stat="PASS"
    elif 60<=T<=69.99:
        grade="C"
        stat="PASS"
    elif 50<=T<=59.99:
        grade="D"
        stat="PASS"
    else:
        grade="F"
        stat="FAIL"
else:
    print(f"Invalid Score")                
print(f"Student Name:{students[0]}\nAssignment Score:{ass[0]}\nMidterm Exam:{mid[0]}\nFinal Exam Score:{fin[0]}\nTotal Score:{T:.2f}\nPercentage:{T/100:.2%}\nGrade:{grade}\nAcadamic Status:{stat}\n{"-"*100}")
T=(ass[1]*0.2)+(mid[1]*0.3)+(fin[1]*0.5)
if 0<=T<= 100:
    if 90<=T<=100:
        grade="A⁺"
        stat="PASS"
    elif 80<=T <=89.99:
        grade="A"
        stat="PASS"
    elif 70<=T<=79.99:
        grade="B"
        stat="PASS"
    elif 60<=T<=69.99:
        grade="C"
        stat="PASS"
    elif 50<=T<=59.99:
        grade="D"
        stat="PASS"
    else:
        grade="F"
        stat="FAIL"
else:
    print(f"Invalid Score")
print(f"Student Name:{students[1]}\nAssignment Score:{ass[1]}\nMidterm Exam:{mid[1]}\nFinal Exam Score:{fin[1]}\nTotal Score:{T:.2f}\nPercentage:{T/100:.2%}\nGrade:{grade}\nAcadamic Status:{stat}\n{"-"*100}")
T=(ass[2]*0.2)+(mid[2]*0.3)+(fin[2]*0.5)
if 0<=T<= 100:
    if 90<=T<=100:
        grade="A⁺"
        stat="PASS"
    elif 80<=T <=89.99:
        grade="A"
        stat="PASS"
    elif 70<=T<=79.99:
        grade="B"
        stat="PASS"
    elif 60<=T<=69.99:
        grade="C"
        stat="PASS"
    elif 50<=T<=59.99:
        grade="D"
        stat="PASS"
    else:
        grade="F"
        stat="FAIL"
else:
    print(f"Invalid Score")
print(f"Student Name:{students[2]}\nAssignment Score:{ass[2]}\nMidterm Exam:{mid[2]}\nFinal Exam Score:{fin[2]}\nTotal Score:{T:.2f}\nPercentage:{T/100:.2%}\nGrade:{grade}\nAcadamic Status:{stat}\n{"-"*100}")
T=(ass[3]*0.2)+(mid[3]*0.3)+(fin[3]*0.5)
if 0<=T<= 100:
    if 90<=T<=100:
        grade="A⁺"
        stat="PASS"
    elif 80<=T <=89.99:
        grade="A"
        stat="PASS"
    elif 70<=T<=79.99:
        grade="B"
        stat="PASS"
    elif 60<=T<=69.99:
        grade="C"
        stat="PASS"
    elif 50<=T<=59.99:
        grade="D"
        stat="PASS"
    else:
        grade="F"
        stat="FAIL"
else:
    print(f"Invalid Score")
print(f"Student Name:{students[3]}\nAssignment Score:{ass[3]}\nMidterm Exam:{mid[3]}\nFinal Exam Score:{fin[3]}\nTotal Score:{T:.2f}\nPercentage:{T/100:.2%}\nGrade:{grade}\nAcadamic Status:{stat}\n{"-"*100}")
T=(ass[4]*0.2)+(mid[4]*0.3)+(fin[4]*0.5)
if 0<=T<= 100:
    if 90<=T<=100:
        grade="A⁺"
        stat="PASS"
    elif 80<=T <=89.99:
        grade="A"
        stat="PASS"
    elif 70<=T<=79.99:
        grade="B"
        stat="PASS"
    elif 60<=T<=69.99:
        grade="C"
        stat="PASS"
    elif 50<=T<=59.99:
        grade="D"
        stat="PASS"
    else:
        grade="F"
        stat="FAIL"
else:
    print(f"Invalid Score")
print(f"Student Name:{students[4]}\nAssignment Score:{ass[4]}\nMidterm Exam:{mid[4]}\nFinal Exam Score:{fin[4]}\nTotal Score:{T:.2f}\nPercentage:{T/100:.2%}\nGrade:{grade}\nAcadamic Status:{stat}\n{"="*100}\n==")
# stage 5
print(f"{"_"*100}\n{"="*100}\n==\n{"ABC COLLEGE":^50}\n{"STUDENT MANGMENT SYSTEM":^50}\n{"="*100}\n==")
print(f"{"COLLEGE INFORMATION":^}\n{"-"*60}\nCollege Name:{college_infos[0]}\nLocation:{college_infos[1]}\nEstablished:{college_infos[2]}\nCollege Code:{college_infos[3]}")
print(f"{"-"*60}\nSTUDENT INFORMATION\n{"-"*60}")
print(f"Student ID:{1001}\nStudent Name:{students[0]}\nStudent Age:{20}")
print(f"{"-"*60}\nCOURSE ENROLLMENT\n{"-"*60}")
print(f"1.{python_programming}\n2.{mathematics}\nTotal Courses: 2")
print(f"{"-"*60}\nEXAMINATION RESULTS\n{"-"*60}")
T=(ass[0]*0.2)+(mid[0]*0.3)+(fin[0]*0.5)
print(f"Student Name:{students[0]}\nAssignment Score:{ass[0]}\nMidterm Exam:{mid[0]}\nFinal Exam Score:{fin[0]}\nTotal Score:{T:.2f}\nPercentage:{T/100:.2%}\nGrade:{grade}\nAcadamic Status:{stat}")
print(f"{"-"*60}\nCOURSE ANALYSIS\n{"-"*60}")
print(f"Python Enrollment:{len(python_programming)}students\nMathematics Enrollment:{len(mathematics)}students\nEngineering Enrollment:{len(computer_engineering)}students\nTotal Unique Students:{len(python_programming|mathematics|computer_engineering)}")
print(f"{"-"*60}\nSTUDENT SUMMERY\n{"-"*60}")
print(f"Registerd Students:{len(students)}\nSelected Student:{students[0]}\nRegestration Status:ACTIVE\nAcadamic Status:{stat}")
print(f"{"="*100}\n==\n{"END OF STUDENT REPORT":^100}\n{"="*100}\n==")



