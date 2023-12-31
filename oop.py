class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.Email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1
    def fullname(self):
        return "{}".format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


print(Employee.num_of_emps)
emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_1.set_raise_amount(1.01)

print(Employee.raise_amount)
print(emp_1.fullname())
print(emp_2.raise_amount)
print(Employee.fullname())



