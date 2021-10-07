# create a class instance of an employee 
class Employee:
    def __init__(self, first_name, last_name, email, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary
    
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp1 = Employee('Brain', 'Paul', 'brainpaul@gmail.com', 70000)
print (emp1.email)
print (emp1.full_name())
print(Employee.full_name(emp1))