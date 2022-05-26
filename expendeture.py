exp = -1
total = 0
max_exp = 0
min_exp = 0
while exp!=0:
    exp = int(input("Enter Expendeture "))
    total = total + exp
    if exp>max_exp:
        max_exp=exp
    else:
        min_exp=exp

print(total)
print(max_exp)
print(min_exp)
