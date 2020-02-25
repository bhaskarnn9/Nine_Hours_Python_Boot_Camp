def my_dictionary() :
	a=[1,2,3,4,5,6,7,8,9]
	print(a[1::3])

def my_dictionary_1() :
	a = [1,2,3,4,5,6,7,8,9]
	b = [10,20,30,40,50]
	print(a[::1])
	print(a)
	print(b)

# prints everything in the set backwards from the given index 
def my_dictionary3() :
	a=[1,2,3,4,5]
	x = len(a)
	print(a[len(a)-1::-1])

my_dictionary3()

my_dictionary4 = {"apple":"$1.99", "orange":"0.99", "avacado":"2.99", "no_of_apples":10, "store_length":9.9, "fruits":["apple", "orange", "avacado"], "dictionary":{"key1":"ohello", "key2":"there", "key3":"its", "key4":"not", "key5":"me"}}

print(my_dictionary["dictionary"])
print("\n")
print(my_dictionary["dictionary"]["key5"])
print(my_dictionary["dictionary"]["key1"])
print(my_dictionary["dictionary"]["key3"])
print(my_dictionary["dictionary"]["key2"])
print(my_dictionary["dictionary"]["key4"])

my_dictionary4()