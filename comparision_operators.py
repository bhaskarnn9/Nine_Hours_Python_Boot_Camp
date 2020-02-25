#This example talks about all the basic comaprision operators

x = 2
y = 3

print(x == y)

print(x+1 == y)

print(x < y)

print(x > y)

print(x >= y)

print(x <= y)

print(x != y)

def compare_integors(x, y) :
	if x == y or x < y :
		return 'x is less than or equal to y'
	return 'y is always greater than x'

print(compare_integors(2, 3))


