from entities.base_entity import BaseEntity

class Business(BaseEntity):
    def __init__(self, name, industry):
        super().__init__(name)
        self.industry = industry
    
    def operate(self):
        """Define how the business functions each time step."""
        print(f"{self.name} ({self.industry}) is serving customers.")
