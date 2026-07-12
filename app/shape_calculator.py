class Shape:
    def __init__ (self,color):
        self.color = color

    
    # --- THE ABSTRACT METHOD DEFINITION ---
    def calculate_area(self) -> float:
        """
        Abstract Method: Acts as a structural blueprint.
        Does not contain actual math; forces child classes to override it.
        """
        raise NotImplementedError("Architectural Rule Violation: You must implement calculate_area() in the child class!")