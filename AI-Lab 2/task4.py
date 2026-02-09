class Employee:
    def work(self):
        print("Employee is working...")


class Manager(Employee):
    def work(self):
        print("Manager is planning and supervising the team.")


class Developer(Employee):
    def work(self):
        print("Developer is writing code.")


class Designer(Employee):
    def work(self):
        print("Designer is creating visual designs.")


# Objects
emp1 = Manager()
emp2 = Developer()
emp3 = Designer()

employees = [emp1, emp2, emp3]

for emp in employees:
    emp.work()
