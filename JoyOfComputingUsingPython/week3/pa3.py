from datetime import datetime

name1 = input().strip().capitalize()
dob1 = input().strip()
name2 = input().strip().capitalize()
dob2 = input().strip()

dob1_date = datetime.strptime(dob1, "%d-%m-%Y")
dob2_date = datetime.strptime(dob2, "%d-%m-%Y")
if dob1_date > dob2_date :
    print(name1,end='')
elif dob1_date < dob2_date:
    print(name2,end='')
else:
    print(min(name1,name2),end='')