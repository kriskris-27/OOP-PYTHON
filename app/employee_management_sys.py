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

    def calculate_annual_salary(self):
        return super().calculate_annual_salary()

class Intern(Employee):
    def __init__(self,id,name,hourly_rate,hours_worked):
        super().__init__(name,id,initial_salary=0)

        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_annual_salary(self):
        return self.hourly_rate*self.hours_worked


def process_payroll(list_of_employees):
    total_company_spend=0 

    for employee in list_of_employees:
        print(f"EMP ID : {employee.id}\n EMP NAME : {employee.name}")
        
        spent = employee.calculate_annual_salary()
        total_company_spend+=spent

    print(f"total company spent : {total_company_spend}")



if __name__ == "__main__":
    
    # Let's create our diverse workforce
    manager_emp = Manager(
        name="Anjali Sharma", 
        id="MGR-001", 
        initial_salary=95000.0,    # ₹95k/month
        department="Engineering", 
        bonus=150000.0             # ₹150k yearly bonus
    )

    developer_emp = Developer(
        name="Krishnakumar S", 
        id="DEV-002", 
        initial_salary=75000.0,    # ₹75k/month
        programming_language=["Python", "FastAPI", "React"]
    )

    intern_emp = Intern(
        name="Rohan Das", 
        id="INT-003", 
        hourly_rate=250.0,         # ₹250 per hour
        hours_worked=480           # Total hours worked over internship
    )

    # Put them all into one uniform tracking bucket
    corporate_workforce = [manager_emp, developer_emp, intern_emp]

    # Hand the folder to our polymorphic accountant tool
    process_payroll(corporate_workforce)