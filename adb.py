print("Start program")

def _return_string():
	x = 10
	y = 20
	if type(x) == int:
		print("x is of type integer")
		x = str(x)
	else:
		print("x is of type string")
	if type(y) == int:
		print("y is of type integer")
		y = str(y)
	else:
		print("y is of type string")
	print("concatenate x and y:",x+y)

def _return_integer():
	x = 10
	y = 20
	if type(x) == str:
		print("x is of type string")
		x = int(x)
	else:
		print("x is of type integer")
	if type(y) == str:
		print("y is of type string")
		x = int(y)
	else:
		print("y is of type integer")
	print("sum of x and y:",x+y)

_return_string()
_return_integer()

print("end program")

my_dictionary = {"key1":"hello_world", "key2":"this_is_my_dictionary"}

print(my_dictionary["key1"])

my_dictionary = {"apple":"$1.99", "orange":"0.99", "avacado":"2.99", "no_of_apples":10, "store_length":9.9, "fruits":["apple", "orange", "avacado"], "dictionary":{"key1":"ohello", "key2":"there", "key3":"its", "key4":"not", "key5":"me"}}

print(my_dictionary["dictionary"])
print("\n")
my_dictionary["dictionary"]["key6"] = "6th_key_value"
print(my_dictionary["dictionary"]["key5"])
print(my_dictionary["dictionary"]["key1"])
print(my_dictionary["dictionary"]["key3"])
print(my_dictionary["dictionary"]["key2"])
print(my_dictionary["dictionary"]["key4"])
print(my_dictionary["dictionary"])
print(my_dictionary["dictionary"]["key6"])


my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[0])

print(len(my_tuple))