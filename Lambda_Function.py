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


# write a lambda function that sums arguments a, b, c
# and prints the result

def _lambda_three_args(a, b, c):
    return lambda l: l + a + b + c


result = _lambda_three_args(1, 2, 3)
print(result(0))
