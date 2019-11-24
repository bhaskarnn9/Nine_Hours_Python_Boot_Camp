"""
Things to know: data and functions = attributes and methods (In a Class)
Agenda:
1. create a class
2. understand the difference between a class and an instance of that class
3. create an instance of the class
4. how to initialize class attributes and create methods
"""


# Creating a class called EmptyClass

class EmptyClass:
    pass


# if you ever want to leave a class empty, just put 'pass' in it,
# so Python knows that you want it to leave empty for time being.


'''
We will now create a class called 'Employee'
Class is a blue print for creating instances
Each unique employee that we create using our Employee class will be an instance of that class
'''


class Employee:
    pass


# employee_1, employee_1 are instances of the class Employee
employee_1 = Employee()
employee_2 = Employee()

print(employee_1)
print(employee_2)
'''
output:
<__main__.Employee object at 0x102480a10>
<__main__.Employee object at 0x102480a10>

Observe that each instance is an Employee class object and they both are unique
and both have unique locations in memory: 0x102480a10, 0x102480a10
'''

'''
Instance variables: contain data that is unique to each instance
Example : Let's have employee_1 to have a first name and a last name
'''

employee_1.first_name = 'Mitchell'
employee_1.last_name = 'Johnson'
employee_1.email_address = 'mitch_john@company.com'
employee_1.salary = 50000

employee_2.first_name = 'Benjamin'
employee_2.last_name = 'Stokes'
employee_2.email_address = 'ben_stokes@company.com'
employee_2.salary = 60000

print(employee_1.email_address)
print(employee_2.email_address)


# Observe that attributes first_name, last_name, email etc were created manually.
# Now let us the actual power of class where this manual entry wouldn't be required


class EmployeeRecords:

    # think of this method as initialize or a constructor
    # note that when you create a method in a class, they receive the instance as the first argument automatically
    # by convention, we should call the instance as 'self' in Python, so self is mandatory in methods of a class
    # after self, you could have as many arguments as you like/need
    # in our case we will have first_name, last_name, email and pay
    def __init__(self, first_name, last_name, email_address, salary):
        self.first = first_name
        self.last = last_name
        self.email = email_address
        self.pay = salary

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# what happens is that employee_1 is passed on to init method as self (employee_1 = self, and continues to set all the
# mentioned attributes
# Example: self.first = 'Mitchell'
employee_1 = EmployeeRecords('Mitchell', 'Johnson', 'mitch_john@company.com', 50000)
employee_2 = EmployeeRecords('Benjamin', 'Stokes', 'ben_stokes@company.com', 60000)

print(employee_1.email)
print(employee_2.email)

# key take away is that first, last, email, pay are attributes of the class EmployeeRecords

# Now lets add the ability to perform some action, we can add methods to that in our class
# Lets consider adding the ability to display Full Name of the employee

# Method:1 (Manually as following)
print('{} {}'.format(employee_1.first, employee_1.last))

# Method:2 {Automatically as follows)
'''
This is the method called, notice how instead of employee_1.first self.first was used
Because, it would work for any instance in the class
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
Also, notice that () is need to call method fullname, otherwise it would be regarded as calling an attribute
Therefore you if call fullname with (), it prints the method instead of the return value of the method
output: <bound method EmployeeRecords.fullname of <__main__.EmployeeRecords object at 0x108749fd0>>
'''
print(employee_2.fullname())
# output: Benjamin Stokes

'''
Hence, we have achieved full code re-usage.
'''

print(employee_2.pay)

'''
Bonus: We can also call the methods in the class using the Class name itself. which makes it a bit obvious of what's
going on in the back ground
'''

# Example
print(employee_2.fullname())
# Alternative method call
print(EmployeeRecords.fullname(employee_2))

'''
What's really happening is that employee_2.fullname() is getting transformed to EmployeeRecords.fullname(employee_2) by 
passing in object employee_2
'''

'''
Synopsis of what we learnt here:
1. creating a class
2. difference between a class and an instance of that class
3. how to initialize class attributes and create methods
'''

