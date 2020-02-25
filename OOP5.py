# Special (Magic/Dunder) methods
# Operator overloading

class Employee:

    employee_count = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.email_address = self.first_name + '.' + self.last_name + '@company.com'
        self.salary = pay
        
        Employee.employee_count += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    def __repr__(self):
        return 'Employee(\'{}\', \'{}\', \'{}\')'.format(self.first_name, self.last_name, self.salary)

    def __str__(self):
        return 'Employee details: {}, {}'.format(self.fullname(), self.email_address)


class Developer(Employee):
    pass

dev_1 = Developer('Keerthi', 'Chandra', 80000)

print(str(dev_1))

print(repr(dev_1))