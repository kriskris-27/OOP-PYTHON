class Vehicle:
    def __init__(self, make: str, model: str, year: int, daily_rate: float):
        self.make = make
        self.model = model
        self.year = year
        self.is_rented = False  # The availability state tracking flag
        
        self._daily_rate = None
        self.daily_rate = daily_rate

    # --- Encapsulation Gateway for Daily Rental Rate ---
    @property
    def daily_rate(self) -> float:
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value: float):
        if value <= 0:
            raise ValueError("Daily rental rate must be greater than zero.")
        self._daily_rate = value

    # --- Operational State Methods ---

    def rent(self):
        """Attempts to transition the vehicle state from available to rented."""
        # Check for Illegal State Transition:
        if self.is_rented:
            raise ValueError(f"Transaction Denied: The {self.make} {self.model} is already out on rent.")
        
        # Safe State Transition: Flip the boolean switch
        self.is_rented = True
        print(f"Success: The {self.make} {self.model} has been successfully rented out.")

    def return_vehicle(self):
        """Attempts to transition the vehicle state from rented back to available."""
        # Check for Illegal State Transition:
        if not self.is_rented:
            raise ValueError(f"System Error: The {self.make} {self.model} was not checked out. Cannot return.")
        
        # Safe State Transition: Flip the boolean switch back
        self.is_rented = False
        print(f"Success: The {self.make} {self.model} has been safely returned to the garage lot.")

    def calculate_rental_cost(self, days: int) -> float:
        """Calculates total billing cost based on days and the encapsulated rate."""
        # Input Validation Guard:
        if days <= 0:
            raise ValueError("Billing Error: Rental duration must be at least 1 day.")
            
        # Code level: 'self.daily_rate' fires the property getter to fetch the price vault
        return self.daily_rate * days