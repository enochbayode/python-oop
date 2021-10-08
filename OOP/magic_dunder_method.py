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

    def __repr__(self):
        return 'Name is {} {} \n salary is {}'.format(self.first_name, self.last_name, self.salary)

    def __str__(self) -> str:
        return  '{} - {} {}'.format(self.full_name(), self.email, self.salary)

emp1 = Employee('Brain', 'Paul', 'brainpaul@gmail.com', 70000)
print(repr(emp1))
print(str(emp1))