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