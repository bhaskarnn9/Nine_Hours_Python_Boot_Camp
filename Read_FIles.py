# before reading files, let us look at prompt for user input
from builtins import ValueError


def _prompt_user_for_input():
    print('Welcome to age prediction!')
    x = 1
    while x > 0:
        age = input("please enter your age: ")
        try:
            age = int(age)
            if type(age) is not int:
                print('age entered is not a number. Please re-enter: ')
            else:
                num = age + 3
                print(f'Congrats! 3 years later your age will be {num}.')
                break
        except ValueError as e:
            print(e)
    print('Age prediction is done. Cheers!')


def _run_from_terminal():

    from sys import argv
    filename = argv[0]
    name = argv[1]
    place = argv[2]
    text = open('sample.txt')
    print(f'Here\'s your name: {filename}.')
    print('\n')
    print(text.read())
    print('\n')
    print(f'This text file {filename} was written by {name} at {place}')


def _sample():
    import sys
    print("Python version")
    print(sys.version)
    print("Version info.")
    print(sys.version_info)


my_list = [1, 2, 3, 4, 5]

print(help(my_list.insert))





