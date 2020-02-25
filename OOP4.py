# Inheritance - Creating Subclasses
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
    
#Inherit the properties of Employee class to echa sub-class
class Developer(Employee):
    raise_amt = 1.1
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.skill = prog_lang

class UX_Designer(Employee):
    pass

class QA(Employee):
    pass

class CyberSec(Employee):
    raise_amt = 1.2

class Mechanical(Employee):
    pass

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print('--->>', emp.fullname())


# Create instance of eachsub class - which inturn is an instance of the Parent class
dev_1 = Developer('Keerthi', 'Chandra', 80000, 'Java')
des_1 = UX_Designer('Vamshi', 'Krishna', 75000)
des_2 = UX_Designer('Naveen', 'Reddy', 75000)
test_1 = QA('Bhaskar', 'Neella', 70000)
sec_1 = CyberSec('Gautham', 'Soma', 85000)
mech_1 = Mechanical('Manoj', 'Reddy', 65000)

mgr_1 = Manager('Vinay', 'Gurram', 65000, [dev_1, des_1, des_2])
print(mgr_1.email_address)
print(mgr_1.print_emp())
mgr_1.remove_employee(des_1)
print(mgr_1.print_emp())