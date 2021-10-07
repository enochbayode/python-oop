# # create a class instance of an employee 
# class Employee:

#     raise_amount = 1.05
#     num_of_employees = 0

#     def __init__(self, first_name, last_name, email, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.salary = salary
#         Employee.num_of_employees += 1

#     def full_name(self):
#         return '{} {}'.format(self.first_name, self.last_name)
    
#     def apply_raise(self):
#         self.pay = int(self.salary * self.raise_amount)
#         return self.pay
    
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount


# emp1 = Employee('Brain', 'Paul', 'brainpaul@gmail.com', 70000)
# # print (emp1.email)
# # print(emp1.apply_raise())
# # print (Employee.num_of_employees)
# print (Employee.set_raise_amt)


# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)
	
	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print (person1.age)
print (person2.age)

# print the result
print (Person.isAdult(22))
