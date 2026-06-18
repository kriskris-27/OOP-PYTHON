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


