a = 10
#  definition of  A variable is created the moment you first assign a value to it.
"""To know the variable data type"""
print(type(a))
#  out put is <class 'int'>
print('Hai QA', a)
#  Comments
# print('Hai QA'+a) its is not work due to TypeError: can only concatenate str (not "int") to str
""" reason is 
string can't add with integer value, here is string value is Hallo QA and a is integer
Solution convert integer to string 
"""
# """ Is Called multiline string  we can use to commenting and also as Text"""
multi_text = """Reason is 
string can't add with integer value, here is string value is Hallo QA and a is integer
Solution convert integer to string 
"""

# To know length of a variable
print("Length of the Text is", len(multi_text))
print(multi_text)
sp =multi_text.split()
print(sp)
print(type(sp))
print(len(sp))
m=20

b = ++m

print(m)
print(b)
# VARIABLE can Assign Multiple Value
"""Many Values to Multiple Variables"""
x,y,z = "Ajmal", "Basith", "Rana"
print(x)
print(type(x))
print(y)
print(z)
# One Value to Multiple Variables
q=w=e = "Ajmal"
print(q)
print(w)
print(e)
print(type(e), len(e)) # op =<class 'str'> 5
print("Another way to declare a tuple")
tup = 'hai',1,'business'
print(tup)
print(len(tup))
print(type(tup))

space = "              Return the string without any whitespace at the beginning or the end."
# op : Return the string without any whitespace at the beginning or the end.
print(space.strip())
u = "Convert the value of txt to upper case."
print(u.upper()) # OP : CONVERT THE VALUE OF TXT TO UPPER CASE.
print(u.lower()) # OP :convert the value of txt to upper case.

# Dictionary
