# set : an unordered collection of items; therefore make sure to place unique items

# empty set
empty_set = {}

# sample set - notice how set doesn't have key value
sample_set = {1, 2, 3, 4, 5}

# union - returns a set with unique items from all the sets in question
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = {7, 6, 5}
# print(set_1 | set_2 | set_3)
# output: {1, 2, 3, 4, 5, 6, 7}

# intersection : returns a set with common items in all the sets in question
set_1 = {1, 2, 3}
set_2 = {1, 'c', 3}
set_3 = {'x','c', 3}
# print(set_1 & set_2 & set_3)
# output: {3}

# difference : will return a set with unique items in FIRST set
set_1 = {1, 'c', 3}
set_2 = {1, 'b', 3}
# print(set_1 - set_2)
# # output: {'c'}

