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
            Ra

