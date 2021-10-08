# create a class instance of an employee 
class Employee:

    raise_amount = 1.05
    num_of_employees = 0

    def __init__(self, first_name, last_name, email, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary
        Employee.num_of_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.pay = int(self.salary * self.raise_amount)
        return self.pay

#the developer class inherit the employee class   
class Developer(Employee):
    raise_amount = 1.08

    def __init__(self, first_name, last_name, email, salary, prog_lang):
        # super handles the inheritance of first_name, last_name, email, salary
        # from the employee class
        super().__init__(first_name, last_name, email, salary)

        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first_name, last_name, email, salary, employees=None):
        # super handles the inheritance of first_name, last_name, email, salary
        # from the employee class
        super().__init__(first_name, last_name, email, salary)

        # emp are the employees monitored by the manbager
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp  not in self.employees:
            self.employees.append(emp)

        print ("This Employee already exsit in the database")
    
    def remove_emp(self, emp):
        if emp not in self.employees:
            print ("This employee doesn\'t exsit in the database")

        self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(self.employees.fullname)

emp1 = Employee('Brain', 'Paul', 'brainpaul@gmail.com', 70000)
dev1 = Developer('Brain', 'Paul', 'brainpaul@gmail.com', 90000, 'python')
Mag = Manager('John', 'Doe', 'johndoe@gmail.com', 50000, 'Jason')
# print (emp1.email)
emp = 'Mason'
# print(emp1.apply_raise())
print (Manager.add_emp)
# print (Manager.full_name(Mag))
