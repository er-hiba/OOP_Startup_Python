class Employee() :
    def __init__(self, name, sales, bonus_hrs, base_salary):
        self.name = name
        self.sales = sales
        self.bonus_hrs = bonus_hrs
        self.base_salary = base_salary

    def info(self):
        print(f"The employee {self.name} made {self.sales} sales, worked {self.bonus_hrs} bonus hours, \
and \ntheir base salary is {self.base_salary}.")

emp1 = Employee("Joey", 500, 16, 2000)
emp2 = Employee("Mohamed", 1000, 20, 4000)

emp1.info()
emp2.info()
