'''

###
chapter 1.variables and types

 # integers
myint = 7
print(myint)

# decimals/floating point numbers
myfloat = 7.0
print(myfloat)
print(float(myint))

# how to change decimals to integers?

# string
mystr =  'world'
print(mystr)

# single operators
a = 10
b = 20
print(a+b)

c = 'hello'
d = 'world'
print('\"'+ c + ' ' + d + '\"')

e, f = 200, 300
print(e+f)

g, k = 'hello', 'shenzhen'
print(g+k)

# isinstance
mystring = 'hello'
myfloat = 10.0
myint = 20
if  isinstance(mystring, str) and mystring == 'hello':
    print("string:%s" % mystring) # %s for string formatting
if isinstance(myfloat, float) and myfloat == 10.0:
    print("float:%f" % myfloat) # %f for float formatting
if isinstance(myfloat, float) and myfloat == 10.0:
    print("float:%.1f"% myfloat )
if isinstance(myint, int) and myint == 20:
    print("Integer:%d" % myint) # %d for integer formatting

# use f-string instead
print("F-string method output:")
print(f"string:{mystring}")
print(f"float,{myfloat}")
print(f"integer, {myint}")

# isinstance
x = isinstance(1000, (str, float, int, dict, tuple ))
print(x)

'''

### chapter 2. lists
# list can include any types and unlimited variables.
# append fucntion
'''
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[2])
for x in mylist:
    print(x)


# exercise
numbers = []
strings = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)

strings.append('hello')
strings.append('world')
print(strings)

print("the second name in the strings list is %s" %strings[1])
'''
'''
###Chapter 3. Basic operators
# arithmetic operators: addition, subtraction, multiplication, division operator
number = 1+3/2*5
print(number)

intremainder = 14%3
print(intremainder) # 余数

square = 7 ** 2
cube = 3 ** 3
print(square, cube)

# Using operators with strings
string = 'hello' + ', ' + 'world ' + 'welcome'
print(string)
# subtr =  string - 'welcome' ## python only support addition operators for strings.

# multiply strings to form a string with repeated sequence.
mulstr = 'hello' * 10
print(mulstr)

# Using operators with lists
odd = [1, 3, 5]
even = [2, 4, 6]
all = odd + even
print(odd, even, all)
print(all*3)

x_list = []
y_list = []
x_list.append('x')
y_list.append('y')
x_list =  x_list*10
y_list = y_list*10
print(x_list, y_list)
print("X list contains %d objects" % len(x_list))
biglist = x_list + y_list
print(biglist)
# testing code:.count() function
if x_list.count('x') == 10 and y_list.count('y') == 10:
    print("Great ")

x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
'''

# chapter 4: string formatting
# argument specifiers: %s-string, %d-integers, %f-floating, %.1,2,3f-floating numbers with specified digits. %x/%X integers in lower/higher case.
'''
name = "Jone"
print ("Hello, %s!" % name)

# use a tuple to use multiple argument specifiers.
age = 23
print("%s is %d years old." % (name, age))

mylist = [2, 3, 4]
print("a list: %s" % mylist)
# chapter 5: basic string operations

myint = 49.2
print("my integer is %d" % myint)

#exercise: Hello John Doe. Your current balance is $53.44.
name = "Jone Doe"
bal = 53.44
print("Hello %s, your current balance is %d." % (name, bal))
'''

# chapter 5: basic string operations
'''
astring = "Hello, PKU"
print(len(astring))
print(astring.index('K'))
print(astring.count('l'))
print(astring[2:9]) # index includes both spaces and punctuations.
print(astring[::-1])
print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello")) # logical judgement
print(astring.endswith("asdf"))

print(astring.split(" ")) # split and return in a list
'''

# exercise
s = "Hello, world1"

# chapter 6 conditions


# loops
