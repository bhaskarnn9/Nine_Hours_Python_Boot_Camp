# Tuple is a immutable data type; similar to a string or an integer

myTuple = ('a', 'b', 'c', 'd', 'e')


# concatenation - Add two string/char
def _concatenate_tuple():
    my_tuple = ('a', 'b', 'c', 'd', 'e')
    my_tuple_extra = ('f', 'g')
    my_tuple += my_tuple_extra
    return my_tuple


# repetition - duplicate string/char by desired number of times
def _repetition():
    my_tuple = ('a', 'b', 'c', 'd', 'e')
    return my_tuple


# indexing - returns the char/string at given index - I like to call it fetching by index
def _indexing():
    my_tuple = ('a', 'b', 1, 'd', 'e')
    return my_tuple[1]


# slicing - returns specific set of chars or a string from the input-string
def _slicing():
    my_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    return my_tuple[1]  # or [1:-2]
    # remember that since we are slicing a tuple, the output will also be a tuple (if sliced more than one char)


print(_indexing())
