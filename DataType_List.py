# Sequence of mutable Python data type define din []


def _example_list():
    my_list = ['a', '10', 'data', 3.14, None]
    return my_list


# concatenation
def _concatenation():
    my_list = ['a', '10', 'data', 3.14]
    my_list2 = ['python', 22]
    my_list += my_list2
    return my_list
    # output: ['a', '10', 'data', 3.14, 'python', 22]


# remove
def _remove():
    my_list = ['a', '10', 'data', 3.14]
    my_list.remove('data')
    return my_list
    # output: ['a', '10', 3.14]


# repetition
def _repetition():
    my_list = ['a', '10', 'data', 3.14]
    return 2*my_list
    # output: ['a', '10', 'data', 3.14, 'a', '10', 'data', 3.14]


# slicing
def _slicing():
    my_list = ['a', '10', 'data', 3.14]
    return my_list[0:2]
    # output: ['a', '10']


# append
def _append():
    my_list = ['a', '10', 'data', 3.14]
    my_list.append('hi')
    return my_list


def _append2():
    my_list = ['a', '10', 'data', 3.14]
    new_list = ['X', 'Y']
    my_list.append(new_list)
    return my_list
    # output: ['a', '10', 'data', 3.14, ['X', 'Y']]


# extend
def _extend():
    my_list = ['a', '10', 'data', 3.14]
    my_list.extend(['X', 'Y'])
    return my_list
    # output: ['a', '10', 'data', 3.14, 'X', 'Y']


# insert
def _insert():
    my_list = ['a', '10', 'data', 3.14, 'X', 'Y']
    my_list.insert(2, 30)
    return my_list


print(_insert())
