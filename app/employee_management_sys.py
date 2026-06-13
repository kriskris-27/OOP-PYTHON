class Employee:
    """Base class representing a generic employee."""
    
    def __init__(self, name: str, employee_id: str, salary: float):
        self.name = name
        self.employee_id = employee_id
        self._salary = None  # Internal attribute for encapsulation
        self.salary = salary  # Triggers the setter validation

    @property
    def salary(self) -> float:
        """Getter for salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float):
        """Setter for salary with strict positive validation."""
        if value < 0:
            raise ValueError("Salary must be a positive number.")
        self._salary = value

    def calculate_annual_salary(self) -> float:
        """Calculates the standard annual baseline salary."""
        return self.salary * 12

    def give_raise(self, percentage: float):
        """Increases the base monthly salary by a given percentage."""
        if percentage <= 0:
            raise ValueError("Raise percentage must be greater than zero.")
        self.salary += self.salary * (percentage / 100)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ID: {self.employee_id} | Name: {self.name}"


class Manager(Employee):
    """Child class representing a Manager with a specific department and annual bonus."""
    
    def __init__(self, name: str, employee_id: str, salary: float, department: str, bonus: float):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.bonus = bonus

    def calculate_annual_salary(self) -> float:
        """Overrides base method: Includes the fixed annual bonus."""
        base_annual = super().calculate_annual_salary()
        return base_annual + self.bonus


class Developer(Employee):
    """Child class representing a Developer with a set of programming languages."""
    
    def __init__(self, name: str, employee_id: str, salary: float, programming_languages: list):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages

    def calculate_annual_salary(self) -> float:
        """Overrides base method: Standard calculation (can be customized if tech stack bonuses apply)."""
        return super().calculate_annual_salary()


class Intern(Employee):
    """Child class representing an Intern paid on an hourly basis."""
    
    def __init__(self, name: str, employee_id: str, hourly_rate: float, hours_worked: float):
        # Interns have an hourly structure; initializing base monthly salary to 0
        super().__init__(name, employee_id, salary=0.0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_annual_salary(self) -> float:
        """Overrides base method: Calculates annual earnings based purely on hourly metrics."""
        return self.hourly_rate * self.hours_worked


# --- Polymorphic Payroll Processing ---

def process_payroll(employees: list[Employee]):
    """
    Processes and prints the payroll for a list of diverse employees.
    Demonstrates Polymorphism by calling calculate_annual_salary() 
    and accessing attributes uniformly, regardless of the underlying subclass.
    """
    print(f"\n{'='*20} RUNNING ANNUAL PAYROLL {'='*20}\n")
    total_payroll = 0.0
    
    for emp in employees:
        annual_pay = emp.calculate_annual_salary()
        total_payroll += annual_pay
        
        print(emp)
        print(f" -> Calculated Annual Payout: ₹{annual_pay:,.2f}")
        
        # Displaying class-specific data safely if needed
        if isinstance(emp, Manager):
            print(f"    Department: {emp.department} | Bonus Included: ₹{emp.bonus:,.2f}")
        elif isinstance(emp, Developer):
            print(f"    Languages: {', '.join(emp.programming_languages)}")
        elif isinstance(emp, Intern):
            print(f"    Hourly Metrics: {emp.hours_worked} hrs @ ₹{emp.hourly_rate}/hr")
        print("-" * 64)
        
    print(f"\nTotal Annual Payroll Expenditure: ₹{total_payroll:,.2f}")
    print(f"{'='*64}")


# --- Execution Hook / Test Suite ---
if __name__ == "__main__":
    # 1. Initialization and Encapsulation check
    try:
        invalid_emp = Employee("Test Fail", "EMP000", -5000)
    except ValueError as e:
        print(f"Encapsulation Guard Verified: {e}")

    # 2. Creating instances of diverse subclasses
    mgr = Manager("Anjali Sharma", "MGR001", 95000.0, "Engineering", 150000.0)
    dev_1 = Developer("Krishnakumar", "DEV002", 75000.0, ["Python", "TypeScript", "Go"])
    dev_2 = Developer("Rohan Das", "DEV003", 68000.0, ["Java", "Spring Boot"])
    intern = Intern("Amit Rao", "INT004", 450.0, 480.0)  # 480 hours total tracking

    # 3. Apply a performance raise to a developer
    print(f"\nApplying 10% raise to {dev_1.name}...")
    dev_1.give_raise(10)

    # 4. Compile into a uniform list to execute polymorphic payroll
    corporate_team = [mgr, dev_1, dev_2, intern]
    process_payroll(corporate_team)