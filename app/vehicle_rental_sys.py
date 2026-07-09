class Vehicle:
    def __init__(self,make,model,year,daily_rate):
        self.make = make
        self.model = model
        self.year = year

        self.is_rented = False


        self._daily_rate = None

        self.daily_rate = daily_rate


    @property
    def daily_rate(self):
        return self._daily_rate


    @daily_rate.setter
    def daily_rate(self,value):
        if value<=0:
            raise ValueError ("Daily rental rate must be greater than zero.")
        self._daily_rate=value

    
    def rent(self):
        if self.is_rented:
            raise ValueError(f"{self.make} {self.model} is already out for rent")
        self.is_rented = True
        print(f"{self.make} {self.model} Checked out succesfully.")
        


    def return_vehicle(self):
        if not self.is_rented:
            raise ValueError(f"{self.make} {self.model} was not rented out.")
        self.is_rented = True
        print(f" -> [RETURNED]: {self.make} {self.model} returned to lot.")

    def calculate_rental_cost(self, days):
        """Standard baseline billing calculations."""
        if days <= 0:
            raise ValueError("Rental duration must be at least 1 day.")
        return self.daily_rate * days


class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate,num_doors,transmission_type):
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

    #method override
    def calculate_rental_cost(self, days):
        base_cost =  super().calculate_rental_cost(days) #including those existing code and adding some additional changes particularly works for this interms of buisness logic
        cargo_surcharge = self.cargo_capacity * 500

        return base_cost + cargo_surcharge 

  
def process_rental_fleet(vehicle_fleet , rental_days):

    total_revenue = 0

    for vehicle in vehicle_fleet:

        try:
            vehicle.rent()
            cost = vehicle.calculate_rental_cost(rental_days)

            total_revenue+=cost
        except ValueError as err:
            print(f" -> [TRANSACTION DENIED]: {err}")
            
        print("-" * 65)

    print(f"TOTAL SYSTEM BATCH REVENUE : ₹{total_revenue:,.2f}\n")
   

        
if __name__ == "__main__":
    car1 = Car("Maruti", "Swift", 2023, 1200.0, num_doors=4, transmission_type="Manual")
    bike1 = Motorcycle("KTM", "Adventure 390", 2024, 1500.0, engine_cc=373, has_helmet=True)
    truck1 = Truck("BharatBenz", "1617R", 2022, 5000.0, cargo_capacity=7.5, requires_license=True)

    my_fleet = [car1,bike1,truck1]

    process_rental_fleet(my_fleet,rental_days=5)
