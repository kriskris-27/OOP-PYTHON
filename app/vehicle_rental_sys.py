class Vehicle:
    """Base class representing a generic rental vehicle."""

    def __init__(self, make: str, model: str, year: int, daily_rate: float):
        # Public fields: Safe to read and change directly from outside
        self.make = make
        self.model = model
        self.year = year
        
        # State Management Flag: Every vehicle starts off as available (Not rented)
        self.is_rented = False

        # 1. Protected Attribute (The Private Vault for pricing)
        self._daily_rate = None
        
        # 2. Triggering the Guard Rail
        # This passes the daily_rate to the setter validation block below.
        self.daily_rate = daily_rate


    # --- Encapsulation Gateway for Daily Rental Rate ---

    @property
    def daily_rate(self) -> float:
        """The Getter: Safely views the daily rental price."""
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value: float):
        """The Setter: Guard rail to ensure the business doesn't lose money."""
        if value <= 0:
            raise ValueError("Business Rule Violation: Daily rental rate must be greater than zero.")
        self._daily_rate = value