    #Operators:operators is used for variables and values.
# 1arithmetical
# 2logical
# 3comparison
# 4assignment
# boolian
x = 23
y = 32
print("addition of {} and {} is {} " .format(x, y,x+y))
print("subtraction of {} and {} is {} " .format(x, y,x-y))
print("divition of {} and {} is {} " .format(x, y,x/y))
print("multiplication of {} and {} is {} " .format(x, y,x*y))
print("exponential of {} and {} is {} " .format(3, 2,3**2 ))
print("modulus of {} and {} is " .format(23, 32,23 % 32) )


#assignment:used a value to a variable:returns bpolian data type
#1,=
#2.+=
x=5
x=x+6
x+=6
#comparison operator
#1.== equals
#2!=not equalt
#3 ,>, <, >= , <=
 # logical operators:used to compine conditional operations
# 1.and
# 2.or
# 3.not
x = 3
y = 2
# and: return True if both condtion is True
print(x > y and  x < 10 )
#or:returns True if one condition is True
print(x > y or x < 10)
#not:returns True if s codition are false
print(not(x > y and x < 10))
print(x+y)
thislist = ["banana","mango","apple"]
thislist[1] ="orange"
print(thislist)
thislist = ["red","yellow","blue"]
x = ("apple","tomato","banana")
y = list(x)
y[1]= "kiwi"
x = tuple(y)
print(x)
thistuple = ("white","black","pink")
for x in thistuple:
    print(x)
thisset = {"book","pen","pencil"}
for x in thisset:
    print(x)

