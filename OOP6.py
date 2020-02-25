# without using property decorator

class Employee1:

    employee_count = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.email_address = self.first_name + '.' + self.last_name + '@company.com'
        self.salary = pay
        
        Employee1.employee_count += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


class Developer1(Employee1):
    pass

dev_1 = Developer1('keerthi', 'chandra', 80000)

print(dev_1.email_address)
# output: email_address

# using property decorator

class Employee2:

    employee_count = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        #self.email_address = self.first_name + '.' + self.last_name + '@company.com'
        self.salary = pay
        
        Employee2.employee_count += 1

    @property
    def email_address(self):
        return '{}.{}@company.com'.format(self.first_name, self.last_name)

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


class Developer2(Employee2):
    pass

dev_2 = Developer2('vamshi', 'krishna', 80000)

print(dev_2.email_address)
# output: vamshi.krishna@company.com
# Note that without @property at method email_address, one would have to make a method call
# with annotation @property, one call call it like an attribute

# using setter

class Employee3:

    employee_count = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        #self.email_address = self.first_name + '.' + self.last_name + '@company.com'
        self.salary = pay
        
        Employee3.employee_count += 1

    @property
    def email_address(self):
        return '{}.{}@company.com'.format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


class Developer3(Employee3):
    pass

dev_3 = Developer3('bhaskar', 'neella', 80000)

print(dev_3.fullname)
print(dev_3.email_address)
dev_3.fullname = 'macbook pro'
print(dev_3.fullname)
print(dev_3.email_address)
# output: vamshi.krishna@company.com

# using setter

class Employee4:

    employee_count = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        #self.email_address = self.first_name + '.' + self.last_name + '@company.com'
        self.salary = pay
        
        Employee4.employee_count += 1

    @property
    def email_address(self):
        return '{}.{}@company.com'.format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)


class Developer4(Employee4):
    pass

dev_4 = Developer4('sunil', 'nalla', 80000)

print(dev_4.fullname)
print(dev_4.email_address)
del dev_4.fullname
print('deleted!', dev_4.fullname)