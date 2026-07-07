class Vehicle:
    def __init__(self,make,model,year,daily_rate,is_rented):
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
        print(f"{self.make} {self.model}Checked out succesfully.")
        


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