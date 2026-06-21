class Employee:
    def __init__ (self,name,id,initial_salary):
        self.name = name
        self.id = id

        self._salary = None

        self.salary = initial_salary


    @property
    def salary(self):
        return self._salary


    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cant be negative")
        self._salary = value

    def calculate_annual_salary(self):
        return self.salary * 12

    def give_raise(self,percentage):
        if percentage <=0:
            raise ValueError("Percentage cant be negative")

class Manager(Employee):
    def __init__(self,name,id,initial_salary,department,bonus):
        super().__init__(name,id,initial_salary)

        self.department = department

        if self.bonus<0:
            raise ValueError("bonus cant be negative")
        
        self.bonus = bonus

    


