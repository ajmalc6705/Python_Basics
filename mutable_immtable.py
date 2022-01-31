
#  ****************** Immutable **************************************
immutable = """ Immutable object mean we can't edit/Change  After creation"""
# Example of Immutable is int,float,string, and Tuple are the example for the Immutable Object
tup = (6,1,2,3)
print(tup)
print(tup[0])
""" Here the out put 6 because we tack the first position of the tuple is 6 """
"""Now we are going to change the tuple first position value 6 to 10"""
# tup[0]=10
print(tup)
""" we got the error     tup[0]=10
TypeError: 'tuple' object does not support item assignment
"""
""" Another example by using string """
message = "Halo Ajmal we are going to outing are you come with us??"
print(message)
""" now Im taking the last 4th value letter is 'u' """
print(message[-4])
"""And change the Letter into Capital Letter U"""
# message[-4] = 'U'
print(message)
# Traceback (most recent call last):
#   File "./mutable_immtable.py", line 21, in <module>
#  message[-4] = 'U'
# TypeError: 'str' object does not support item assignment


#  Mutable
message1 = "Halo Ajmal we are going to outing are you come with us"
# Currently it is a string and immmutable , 1st we convert string to list using split
message1_list = message1.split()
print(message1_list)
print(type(message1_list))
# o/p : ['Halo', 'Ajmal', 'we', 'are', 'going', 'to', 'outing', 'are', 'you', 'come', 'with', 'us']
print(message1_list[-1])
message1_list[-1] = "Us"
print(message1_list)
# O/P is ['Halo', 'Ajmal', 'we', 'are', 'going', 'to', 'outing', 'are', 'you', 'come', 'with', 'Us']

