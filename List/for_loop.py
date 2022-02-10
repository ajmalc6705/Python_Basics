files = ['Avengers1.mp4','Avengers2.mp4', 'Avengers3.mp4', 'Spiderman.mp4']
print(files)
print(files[0])
print(files[1])
print(files[2])
print(len(files))

for y in range(len(files)):
    print(y)
    print(files[y])

# Remove the .mp4 in files
for x in files:
    print(x)
    name = x[0:-4]
    print(name)


# Multiplication table
r = int(input("Enter the Range"))
num = int(input("Enter the Number for the multiplication Table :"))

for r in range(1,r):
    # q = r+1
    res = r * num
    print('%s'q, '*', num, ':', res)


# while num<=10:
#     print(num)
#     for i in str(num):
#         print("*")
#         for j in i:
#             print("\n")
#     num = num+1


