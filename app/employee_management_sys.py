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
    def __init__(self, name, id, initial_salary, department, bonus):
        super().__init__(name, id, initial_salary)
        self.department = department

        
        if bonus < 0:
            raise ValueError("Bonus cannot be negative")
        
        self.bonus = bonus

    # --- METHOD OVERRIDE ---
    def calculate_annual_salary(self):
        """Overrides parent method to include the manager's annual bonus."""
        return super().calculate_annual_salary() + self.bonus

    

class Developer(Employee):
    def __init__(self,name,id,initial_salary,programming_language):
        super().__init__(name,id,initial_salary)

        self.programming_language = programming_language

        

