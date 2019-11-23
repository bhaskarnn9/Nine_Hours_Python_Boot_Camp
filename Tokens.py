# ------------------------------

# Token1 : Keyword


# Keywords are reserved words and cannot be used as variable names
# Run following example and observe the error
# True = 10 # incorrect
print(True)

# ------------------------------

# Token2 : Identifier

# Identifier is a name you give to a variable, function, class or an object
# No character expect ( _ ) can be used in identifier
# case sensitivity applies
Var = 5
var = 10
# observe that var and Var two different variables

# Identifier cannot start with a number

# 1Variable = 1 # incorrect
_1Variable = 1 # correct

# ------------------------------

# Token3 : Literal

# _1. String Literals

name1 = 'John'
name2 = "James"
print(name1)
print(name2)

multi_line = '''string1
string2
string3
end of multi_line'''
print(multi_line)
# output looks like following
'''
string1
string2
string3
end of multi_line
'''

text = 'Hello\
World'
print(text)
# output looks like following
'HelloWorld'

# _2. Numeric Literals

# int(10, -123), long(123456L), float(10.01, -3.01), complex(3.134j)
i = 10
j = 10.1
k = 3.3j

# _3. Boolean Literals

# True, False
key = True
value = False

# _4. Special Literals

# None
string_1 = None
# Equivalent of Null in Java/C

# ------------------------------

# Token4 : Operators

# _1. Arithmetic Operator
# +, -, @, /, %
k = 1 + 2
l = k % 2
print(l)
# here + and % are arithmetic operators

# _2. Assignment Operator

# =, +=, -=, *=
# Arithmetic operation always follows PEDMAS
var = 10
var += 10 # var = var + 10
var -= 10 # var = var - 10
print(var)
# here = and += and -= are assignment operators

# _3. Comparision Operator

# >, < , <=, >=, !=, ==
a = 10
b = 20
print(a > b) # output = False
# here > is comparision operator

# _4. Logical Operator

# and, or and not
a = 10
b = 20
print(a<b and b>a)
# here and is logical operator

# _5. Bitwise Operator

# &, |, >>, <<, ~
print(7 | 5) # output : 7 # | is binary addition
print(7 & 5) # output : 5 # & is binary multiplication

# If you do not know how to do binary conversion, please visit my blog
# https://awesomenessofbinary.blogspot.com/2019/11/ever-see-crazy-binary-number-like.html

print(~7) # output : -8
print(10>>2) # output 2
print(10<<2) # output 40

# _6. Identity Operator

# is, is not
x = 10
print(x is 10) # output : True
print(x is not 10) # output : False

# _7. Membership Operator

# in, not in
flowers = ['rose', 'lilly', 'jasmine']
print('rose' in flowers) # output : True
print('me' in 'case') # output : False

# ------------------------------



