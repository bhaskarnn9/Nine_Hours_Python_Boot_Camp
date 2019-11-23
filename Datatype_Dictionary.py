# empty dictionary
empty_dict = {}

# dictionary with integer keys
int_key_dict = {1: 'apple', 2: 'ball', 3: 'hello'}

# dictionary with mixed keys
mixed_key_dict = {1: 'hello', 'name': 'John', 'X': [2, 3, 4]}

# pairing - from sequence having each item as a pair
pair_dict = dict([('name', 'John'), ('arrival', 3)])
# print(pair_dict)
# output: {'name': 'John', 'arrival': 3}

# accessing dictionary - can be accessed by key
access_dict = {1: 'John', 2: 'Bob', 3: 'Alice'}
# print(access_dict[2])
# output: Bob

# access all keys
access_keys = {1: 'John', 2: 'Bob', 3: 'Alice'}
# print(access_keys.keys())
# output: dict_keys([1, 2, 3])

# access all values
access_values = {1: 'John', 2: 'Bob', 3: 'Alice'}
# print(access_values.values())
# output: dict_values(['John', 'Bob', 'Alice'])

