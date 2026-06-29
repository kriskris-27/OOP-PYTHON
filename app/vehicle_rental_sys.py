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

class Car(Vehicle):
    """Child class representing a specialized Car configuration."""

    def __init__(self, make: str, model: str, year: int, daily_rate: float, num_doors: int, transmission_type: str):
        # Step 1: Pass core specifications up to the Vehicle base class
        super().__init__(make, model, year, daily_rate)
        
        # Step 2: Validate and initialize attributes unique to a Car
        if num_doors <= 0:
            raise ValueError("A car must have at least 1 door.")
            
        self.num_doors = num_doors
        self.transmission_type = transmission_type  # e.g., "Automatic" or "Manual"


class Motorcycle(Vehicle):
    """Child class representing a specialized Motorcycle configuration."""

    def __init__(self, make: str, model: str, year: int, daily_rate: float, engine_cc: int, has_helmet: bool):
        # Step 1: Pass core specifications up to the Vehicle base class
        super().__init__(make, model, year, daily_rate)
        
        # Step 2: Validate and initialize attributes unique to a Motorcycle
        if engine_cc <= 0:
            raise ValueError("Engine displacement (CC) must be a positive integer.")
            
        self.engine_cc = engine_cc
        self.has_helmet = has_helmet  # Safety configuration flag: True/False

class Truck(Vehicle):
    """Child class representing a specialized heavy-duty Truck configuration."""

    def __init__(self, make: str, model: str, year: int, daily_rate: float, cargo_capacity: float, requires_license: bool):
        # Step 1: Pass core metrics up to the Vehicle base class
        super().__init__(make, model, year, daily_rate)
        
        # Step 2: Validate and initialize attributes unique to a Truck
        if cargo_capacity <= 0:
            raise ValueError("Cargo capacity (in tons) must be greater than zero.")
            
        self.cargo_capacity = cargo_capacity      # e.g., capacity in tons (e.g., 3.5, 10.0)
        self.requires_license = requires_license  # Safety flag: True if it requires a heavy vehicle commercial license

    # --- METHOD OVERRIDE ---
    def calculate_rental_cost(self, days: int) -> float:
        """
        Overrides the parent's cost calculation.
        Adds a flat heavy-vehicle maintenance fee based on cargo capacity.
        """
        # Step A: Get the standard baseline cost from the Vehicle parent (daily_rate * days)
        base_cost = super().calculate_rental_cost(days)
        
        # Step B: Apply a heavy equipment surcharge (e.g., ₹500 per ton of capacity)
        heavy_surcharge = self.cargo_capacity * 500.0
        
        return base_cost + heavy_surcharge