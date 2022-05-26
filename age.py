name = input("Enter Your Name ")
age = int(input("enter Your Age "))

year50 = 50 - age
if year50>0:
    print("Hai "+ name.title()+ 'your age is 50 is over '+ str(year50))
else:
    print("Hai "+ name.title() + ' your age allredy  50 is  over '+ str(-year50))