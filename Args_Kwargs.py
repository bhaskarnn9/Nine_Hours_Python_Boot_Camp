# ######################

"""
*args and *kwargs are two functional parameters
that you may encounter when you are looking at
other people's code or any source code.
"""
"""
When you are going to want toi accept an arbitrary number of arguments
and keyword-arguments without having to pre-define a bunch of parameters
in function calls.
"""


# Example1
def my_func(a, b):
    # returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


# print(my_func(40, 60))
# output = 5.0


# Example1 of *args
# *args = TUPLE of parameters coming in
def my_func_args_1(*args):
    return sum(args) * 0.05


print(my_func_args_1(40, 60))
# output = 5.0
print(my_func_args_1(40, 60, 100))


# output = 10.0


# Example2 of *args
def my_func_args_2(*args):
    x = args[0]
    y = args[1]
    return x + y


print(my_func_args_2(40, 60, 100))
# output = 100
# notice how argument 100 is not being used/causing any issue


"""
**kwargs is used handle arbitrary no of key-worded-arguments
**kwargs = DICTIONARY of parameters coming in
"""


# Example1 of **kwargs
def my_func_kwargs_1(**kwargs):
    print(kwargs)
    # output = {'fruit': 'apple', 'veggie': 'lettuce'}
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find my choice of fruit in available fruits')


print(my_func_kwargs_1(fruit='apple'))
# output = My fruit of choice is apple
print(my_func_kwargs_1(veggie='lettuce'))
# output = I did not find my choice of fruit in available fruits
print(my_func_kwargs_1(fruit='apple', veggie='lettuce'))


# output = My fruit of choice is apple
# Notice that fruit in function call is being used as the key in Dictionary of kwargs


# Example2 of **kwargs
# remember that ** is the indicator to Python and not 'kwargs'
def my_func_kwargs_2(**jelly):
    print(jelly)
    # output = {'veggie': 'lettuce', 'fruit': 'apple'}


my_func_kwargs_2(veggie='lettuce', fruit='apple')


# Bonus
def args_kwargs(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


args_kwargs(10, 20, 30, fruit='orange', food='chickens', veggie='lettuce')
# output = I would like 10 chickens
# notice how  20, 30 and fruit='orange', veggie='lettuce' are disregarded

