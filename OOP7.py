# Polymorphism 
# Naive definition: Polymorphism is the ability to assume various forms

# Things to know:
# Overriding is a type of polymorphism

# Method overriding is an OOP feature that allows a subclass to provide a different
# implementation of a method that is already defined by its superclass or by one of
# its superclasses.

class Parrot:

    def fly(self):
        print('Parrot can fly')
    
    def swim(self):
        print('Parrot can\'t swim')


class Penguin:

    def fly(self):
        print('Penguin can\'t fly')
    
    def swim(self):
        print('Penguin can swim')

# common interface
def flying_test(bird):
    bird.fly()
# instanciate objects
par = Parrot()
peg = Penguin()

# pass object to check
flying_test(par)
flying_test(peg)

# output:
# Parrot can fly
# Penguin can't fly

# example 2

def outer_func():
    message = 'hi'

    def inner_func():
        print(message)
    
    return inner_func

my_func = outer_func()