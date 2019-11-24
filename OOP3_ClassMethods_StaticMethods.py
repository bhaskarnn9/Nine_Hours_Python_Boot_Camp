class Methods:
    """
        Agenda:
        1. understand what a regular method is
        2. understand what a class method is
        3. understand what a static method is
        4. understand the difference between each of them
    """
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first_name, last_name, email_address, salary):
        self.first = first_name
        self.last = last_name
        self.email = email_address
        self.pay = salary
        Methods.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Method 1
    def apply_raise(self):
        # 4 % raise
        self.pay = int(self.pay * 1.04)

    def apply_raise_cv(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def class_apply_raise_cv(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            # monday = 0 and so on
            return False
        return True

    '''
    Regular Method:
    We learnt in previous tutorials that regular methods in a class automatically take instance as the first argument
    By convention, we call it self
    '''
    '''
    Class Method:
    So if we are able to change the 'self' to 'class' as the first argument, it is a class method.
    To convert a regular method to a class method, you simply add a decorator @classmethod
    By convention, 'cls' is the first argument in a class method and the rest are user defined
    '''
    '''
    Static Method:
    We are aware that Regular methods pass self(instance) and Class methods pass cls(class) as first argument
    Static methods do not pass either, in other words there's no default argument
    To create a static method in a class, you simply add a decorator @staticmethod
    '''
    '''
    When to use which method:
    Look at the variables that you are going to want to use in a method.
    If you are going to use class variables, it's a good idea to create a class method
    Same rule applies for instance variables
    And when you are not using either class or instance variables, you should go for a static method
    
    '''


employee_1 = Methods('Mitchell', 'Johnson', 'mitch_john@company.com', 50000)
employee_2 = Methods('Benjamin', 'Stokes', 'ben_stokes@company.com', 60000)

Methods.class_apply_raise_cv(1.05)
# We are working with class rather than an instance so it changes the raise_amount to 1.05 for all instances & the class
# Methods.class_apply_raise_cv(1.05) is same as Methods.raise_amount = 1.05
print(Methods.raise_amount)
print(employee_1.raise_amount)
print(employee_2.raise_amount)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Methods.is_workday(my_date))
