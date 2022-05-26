exp = []

stop = False

while not stop:
    num = int(input("Enter Your Expences "))
    if num!=0:
        exp.append(num)
    else:
        stop = True


print(exp)
print("Total Expenses is ", sum(exp))
print("Maximum Expenses is ", max(exp))
print("Minimum Expenses is ", min(exp))