class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


    def set_salary(self, salary):
        try:
            if salary >= 0:
                self._salary = salary
        except ValueError:
            print("Salary has to be given as number!")

a = Employee(1, "Mick", "Jagger")
print(a.id, a.first_name, a.last_name)
a.set_salary(500)
print(a._salary)