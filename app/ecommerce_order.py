class Product:
    """Base class representing a core retail product with strict state encapsulation."""

    def __init__(self, name: str, price: float, stock: int, sku: str):
        self.name = name
        self.sku = sku  # Stock Keeping Unit (Unique Identifier)
        
        # Initialize internal storage containers as hidden slots
        self._price = None
        self._stock = None
        
        # Route the incoming arguments directly through the property setter validation checks
        self.price = price
        self.stock = stock

    # ==========================================
    # 1. ENCAPSULATION GATEWAY: PRICE
    # ==========================================
    @property
    def price(self) -> float:
        """The price getter: Safely fetches the internal price float."""
        return self._price

    @price.setter
    def price(self, value: float):
        """The price setter: Acts as a strict validation guard rail."""
        if value <= 0:
            raise ValueError("Financial Guardrail: Product price must be strictly greater than zero.")
        self._price = value

    # ==========================================
    # 2. ENCAPSULATION GATEWAY: STOCK
    # ==========================================
    @property
    def stock(self) -> int:
        """The stock getter: Safely fetches the current inventory count."""
        return self._stock

    @stock.setter
    def stock(self, value: int):
        """The stock setter: Prevents inventory levels from going negative."""
        if value < 0:
            raise ValueError("Inventory Guardrail: Stock count cannot fall below zero.")
        self._stock = value

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_details(self) -> str:
        return f"Product: {self.name} | Price: ${self.price:.2f}"


class PhysicalProduct(Product):
    def __init__(self, name: str, price: float, weight: float, shipping_cost: float):
        super().__init__(name, price)
        self.weight = weight  # Weight in kg
        self.shipping_cost = shipping_cost

    def total_cost(self) -> float:
        return self.price + self.shipping_cost

    def get_details(self) -> str:
        base_details = super().get_details()
        return f"{base_details} | Weight: {self.weight}kg | Shipping: ${self.shipping_cost:.2f}"


class DigitalProduct(Product):
    def __init__(self, name: str, price: float, download_url: str, file_size: float):
        super().__init__(name, price)
        self.download_url = download_url
        self.file_size = file_size  # Size in MB

    def get_details(self) -> str:
        base_details = super().get_details()
        return f"{base_details} | Download Size: {self.file_size}MB | URL: {self.download_url}"


class SubscriptionProduct(Product):
    def __init__(self, name: str, price: float, billing_cycle: str, duration: int):
        super().__init__(name, price)
        self.billing_cycle = billing_cycle  # e.g., 'Monthly', 'Annually'
        self.duration = duration  # Duration in months

    def get_details(self) -> str:
        base_details = super().get_details()
        return f"{base_details} | Billing Cycle: {self.billing_cycle} | Duration: {self.duration} months"