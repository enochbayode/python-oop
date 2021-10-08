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


emp1 = Employee('Brain', 'Paul', 'brainpaul@gmail.com', 70000)
# print (emp1.email)
print(emp1.apply_raise())
print (Employee.num_of_employees)
# print(Employee.__dict__)
# print (emp1.raise_amount)
# print (emp1.full_name())
# print(Employee.full_name(emp1))