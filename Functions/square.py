# To Define the Square Function
num = int(input("Enter a Number :"))
def square(num):
    return num * num
e

print("Square of the Entered number is ", square(num))

# To Find Sum of the Square of Two Number
x = int(input('Enter the 1st Number :'))
y = int(input('Enter the 2nd Number :'))
def sum_of_square(x,y):
    return square(x) + square(y)


print("Sum of Square root is " + str(sum_of_square(x, y)))

# To Find The Square Root of Given Number
z = int(input("Enter THe Value to get find Square Root :"))
f = square
print(f(x))

# Another Method to find the sum of Squares
j = square
k = int(input("Enter First Number :"))
m = int(input("Enter Second Number :"))

def sum_square(j, k, m):
    return f(k)+f(m)


print(sum_square(j, k, m))
