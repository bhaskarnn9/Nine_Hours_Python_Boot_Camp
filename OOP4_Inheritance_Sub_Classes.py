"""
Agenda:
What is inheritance
What is a sub class
Use inheritance and sub classes meaningfully
"""


# Let us define a parent class

class ParentClassEmployees:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first_name, last_name, email_address, salary):
        self.first = first_name
        self.last = last_name
        self.email = email_address
        self.pay = salary
        self.user_name = self.first + '_' + self.last
        ParentClassEmployees.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Method 1
    def apply_raise(self):
        # 4 % raise
        self.pay = int(self.pay * 1.04)

    def apply_raise_ins(self):
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


employee_1 = ParentClassEmployees('Mitchell', 'Johnson', 'mitch_john@company.com', 50000)
employee_2 = ParentClassEmployees('Benjamin', 'Stokes', 'ben_stokes@company.com', 60000)


class ChildClassDevelopers(ParentClassEmployees):
    raise_amount = 1.1

    def __init__(self, first_name, last_name, email_address, salary, program_lang):
        super().__init__(first_name, last_name, email_address, salary)
        # super().__init__(first_name, last_name, email_address, salary) is same as
        # ParentClassEmployees.__init__(self, first_name, last_name, email_address, salary)
        self.language = program_lang


developer_1 = ChildClassDevelopers('Dhoni', 'Singh', 'dhoni_singh@company.com', 60000, 'Python')
developer_2 = ChildClassDevelopers('Babar', 'Azam', 'babar_azam@company.com', 50000, 'Java')

print(ParentClassEmployees.num_of_employees)
# output = 4
# since we inherited all the methods and class variables from parent, instances created in the child class will be
# treated just like the instances created in the parent class


# Let's give a special raise_amount just to developers and see what it looks like

print(developer_1.pay)
developer_1.apply_raise_ins()
print(developer_1.pay)
print(developer_2.language)
print(employee_1.user_name)


# Create a class 'Managers' that inherit Employees
class ChildClassManagers(ParentClassEmployees):
    def __init__(self, first_name, last_name, email_address, salary, employees=None):
        super().__init__(first_name, last_name, email_address, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('*****', emp.email, '*****')


manager_1 = ChildClassManagers('Daniel', 'Craig', 'daniel_craig@company.com', 90000, [developer_1])

print(manager_1.fullname())
manager_1.add_emp(developer_2)
manager_1.remove_emp(developer_1)
print(manager_1.print_emp())


print(isinstance(manager_1, ChildClassDevelopers))
print(isinstance(manager_1, ChildClassManagers))
print(isinstance(manager_1, ParentClassEmployees))
print('************')
print(issubclass(ParentClassEmployees, ChildClassManagers))
print(issubclass(ChildClassManagers, ParentClassEmployees))
