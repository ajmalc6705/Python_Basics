exp = -1
list= []
total = 0
max_exp = 0
min_exp = 0
while exp!=0:
    exp = int(input("Enter Expendeture "))
    list.append(exp)
    total = total + exp
    if exp>max_exp:
        max_exp=exp
    else:
        min_exp=exp

print(list)
print("Total  Item available in the expendeture is ", len(list))
print("your Total Expendeture is",total)
print('You spend maximum_is', max_exp)
print('your minimum expendeture is ',min_exp)
