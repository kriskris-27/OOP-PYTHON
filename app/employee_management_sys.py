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


def calculate_annual_salary(self) -> float:
        """
        Calculates the standard annual baseline salary.
        """
        # Code level: 'self.salary' triggers the getter to fetch the monthly rate.
        return self.salary * 12

def give_raise(self, percentage: float):
    """
    Increases the base monthly salary by a given percentage.
    """
    if percentage <= 0:
        raise ValueError("Raise percentage must be greater than zero.")
    
    # Code level: Reads current salary (getter), calculates the bump,
    # and attempts to write it back (setter validation check).
    self.salary += self.salary * (percentage / 100)

    class Manager(Employee):
    """Child class representing a Manager with a department and an annual bonus."""

    def __init__(self, name: str, employee_id: str, initial_salary: float, department: str, bonus: float):
        # Step 1: Pass core attributes up to the Employee parent constructor.
        # This builds the name, ID, and the validated monthly _salary vault.
        super().__init__(name, employee_id, initial_salary)
        
        # Step 2: Set up attributes unique to a Manager
        self.department = department
        
        if bonus < 0:
            raise ValueError("Bonus cannot be negative.")
        self.bonus = bonus

    # --- METHOD OVERRIDE ---
    def calculate_annual_salary(self) -> float:
        """
        Overrides the parent's method to include the manager's annual bonus.
        """
        # Step A: Call the parent class's version of this method using super()
        # This calculates: monthly salary * 12
        base_annual_pay = super().calculate_annual_salary()
        
        # Step B: Add the unique manager bonus state to the total
        total_compensation = base_annual_pay + self.bonus
        
        return total_compensation