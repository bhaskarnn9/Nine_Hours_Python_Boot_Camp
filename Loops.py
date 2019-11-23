def _for_loops():
    my_list = ['apple', 2, 'cat', 4, 'elephant']
    for x in my_list:
        print(x)
        if x is 2:
            break


def _example():
    word = 'mac-book-pro'
    for letter in enumerate(word):
        print(letter)


# for loop along with string literal
def _for_loop_string_literal():
    my_list = ['apple', 2, 'cat', 4, 'elephant', 5, 'gandhi']
    for iterable in my_list:
        if iterable is not 'hello_world':
            print(iterable)
        else:
            print(f'something_else: {iterable}')


# tuple unpacking with for loop
def _unpack_tuple():
    my_list = [('num_1', 1), ('num_2', 2), ('num_3', 3)]
    for (item, item2) in my_list:
        print(item)
        print(item2)


# dictionary
def _dictionary():
    d = {'k1':1, 'k2':2, 'k3':3, 'k4':4}
    for key, pair in d.items():
        print(key)
        print(pair)


_dictionary()
