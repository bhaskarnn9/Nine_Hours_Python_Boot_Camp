# example of a lambda function


# example1
x = lambda a: a + 10
result = x(5)
print(result)

# example2
z = lambda x, y: x * y
print(z(2, 4))


# True power of a lambda function over conventional function


def my_func(n):
    return lambda a: a + n


my_sum = my_func(3)
print(my_sum(10))
