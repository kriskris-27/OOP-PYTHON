# =====================================================================
# 1. THE BASE CLASS
# =====================================================================

class Vehicle:
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.is_rented = False  # Starts default available on the lot

        self._daily_rate = None
        self.daily_rate = daily_rate  # Triggers setter verification below

    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if value <= 0:
            raise ValueError("Daily rental rate must be greater than zero.")
        self._daily_rate = value

    # --- Operational State Methods ---

    def rent(self):
        """Transitions state from available to rented."""
        if self.is_rented:
            raise ValueError(f"{self.make} {self.model} is already out on rent.")
        self.is_rented = True
        print(f" -> [RENTED]: {self.make} {self.model} checked out successfully.")

    def return_vehicle(self):
        """Transitions state from rented back to available."""
        if not self.is_rented:
            raise ValueError(f"{self.make} {self.model} was not rented out.")
        self.is_rented = False
        print(f" -> [RETURNED]: {self.make} {self.model} returned to lot.")

    def calculate_rental_cost(self, days):
        """Standard baseline billing calculations."""
        if days <= 0:
            raise ValueError("Rental duration must be at least 1 day.")
        return self.daily_rate * days


# =====================================================================
# 2. THE CHILD CLASSES (Inheritance)
# =====================================================================

class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_doors, transmission_type):
        super().__init__(make, model, year, daily_rate)
        self.num_doors = num_doors
        self.transmission_type = transmission_type


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, engine_cc, has_helmet):
        super().__init__(make, model, year, daily_rate)
        self.engine_cc = engine_cc
        self.has_helmet = has_helmet


class Truck(Vehicle):
    def __init__(self, make, model, year, daily_rate, cargo_capacity, requires_license):
        super().__init__(make, model, year, daily_rate)
        self.cargo_capacity = cargo_capacity
        self.requires_license = requires_license

    # --- METHOD OVERRIDE ---
    def calculate_rental_cost(self, days):
        """Overrides parent method: Adds a heavy vehicle cargo capacity surcharge."""
        base_cost = super().calculate_rental_cost(days)
        cargo_surcharge = self.cargo_capacity * 500.0  # ₹500 per ton surcharge
        return base_cost + cargo_surcharge


# =====================================================================
# 3. FLEET MANAGEMENT SYSTEM (Polymorphism)
# =====================================================================

def process_fleet_rentals(vehicle_fleet, rental_days):
    """Processes a collection of diverse vehicles uniformly via Polymorphism."""
    print(f"\n{'='*20} PROCESSING FLEET TRANSACTIONS {'='*20}\n")
    total_revenue = 0.0

    for vehicle in vehicle_fleet:
        print(f"Processing Asset: {vehicle.year} {vehicle.make} {vehicle.model}")
        
        try:
            # Polymorphic action: Changes availability flag state
            vehicle.rent()
            
            # Polymorphic calculation: 
            # Cars and Bikes run parent math; Trucks run custom override math!
            cost = vehicle.calculate_rental_cost(rental_days)
            print(f" -> Estimated Bill ({rental_days} Days): ₹{cost:,.2f}")
            
            total_revenue += cost

        except ValueError as err:
            print(f" -> [TRANSACTION DENIED]: {err}")
            
        print("-" * 65)

    print(f"TOTAL SYSTEM BATCH REVENUE : ₹{total_revenue:,.2f}\n")


# =====================================================================
# 4. TESTING THE SIMULATION
# =====================================================================
if __name__ == "__main__":
    # Initialize your diverse vehicles
    car1 = Car("Maruti", "Swift", 2023, 1200.0, num_doors=4, transmission_type="Manual")
    bike1 = Motorcycle("KTM", "Adventure 390", 2024, 1500.0, engine_cc=373, has_helmet=True)
    truck1 = Truck("BharatBenz", "1617R", 2022, 5000.0, cargo_capacity=7.5, requires_license=True)

    # Pack them into your fleet tracking array
    my_fleet = [car1, bike1, truck1]

    # Process a 3-day fleet deployment check
    process_fleet_rentals(my_fleet, rental_days=3)