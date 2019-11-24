class EmployeeRecords:
    """
    Agenda:
    1. understand what a class variable is
    2. understand what an instance variable is
    3. use which and when
    4. create class variables
    """
    raise_amount = 1.04
    num_of_employees = 0

    """
    Instance Variables:

    self.first = first_name
        self.last = last_name
        self.email = email_address
        self.pay = salary
        are the instance variables that are set using self argument

        We set first, last, name, email and pay in init method. These are set for each instance of the employee
        that we create
    """
    def __init__(self, first_name, last_name, email_address, salary):
        self.first = first_name
        self.last = last_name
        self.email = email_address
        self.pay = salary
        EmployeeRecords.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Method 1
    def apply_raise(self):
        # 4 % raise
        self.pay = int(self.pay * 1.04)

    def apply_raise_cv(self):
        self.pay = int(self.pay * self.raise_amount)

    '''
        Class variables:

        the variables that are shared among all the instances of a class.
        '''

    '''
    Difference between class and instance variables:

    Instance variables can be unique for each instance like name, email and pay.
    Class variables should be the same for each instance.

    Example:
    Consider a company that gives annual raise to all the employees every year by a fixed percentage of their salary.
    What ever the amount of raise is, it is the same for all, a variable like this is a good candidate for CV.
    '''

    '''
    Method_1 of doing that
    check apply_raise method
    problem: the raise percentage is hard coded and cannot be updated as easily as we'd like
    
    Method2:
    1. introduce a class variable raise_percentage
    2. it can be accessed via EmployeeRecords.raise_amount or self.raise_amount
    '''

    '''
    How can a class variable be accessed by an instance (as in self.raise_amount)
    to understand this behaviour or ability please check: 
    https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2
    '''


employee_1 = EmployeeRecords('Mitchell', 'Johnson', 'mitch_john@company.com', 50000)
employee_2 = EmployeeRecords('Benjamin', 'Stokes', 'ben_stokes@company.com', 60000)


# print(employee_1.pay)
# EmployeeRecords.apply_raise_cv(employee_1)
# print(employee_1.pay)

print(EmployeeRecords.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)
# the class variable num_of_employees should be same for all the instances of the classes
# therefore we use EmployeeRecords.num_of_employees += 1 instead of self.num_of_employees += 1
print(EmployeeRecords.num_of_employees)






