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