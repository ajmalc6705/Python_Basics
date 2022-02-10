# scope of the variables used in functions.
x = 0
y = 0


def incr(x):
    y = x + 1
    return y


incr(int(input("Enter A Number :")))
print(x, y)  # The Output is x= 0,y =0 the values not changing based on the inc()


# Changing the values of x and y inside the function incr won’t effect the values of global x and y

# Changing the values of x and y inside the function incr  effect the values of global x and y

def global_incr(x):
    global y
    y = x + 1
    return y


global_incr(x)
print("Changing Y value based on the Global Variable of x ", x, y)
# First we assign the x and y value is zero, now the value Y of changed based on the Global Variable  the output 0 1
