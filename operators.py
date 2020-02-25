def compare_objects (a, b, c) :
	if (a < b > c) :
		return 'What I said is true'
	else :
		return 'This is incorrect'

print(compare_objects(1, 2, 0)) #true true
print(compare_objects(1, 2, 2)) #true false
print(compare_objects(3, 2, 2)) #false false
print(compare_objects(3, 2, 1)) #false true