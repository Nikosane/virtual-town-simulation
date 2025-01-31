from entities.base_entity import BaseEntity

class Resident(BaseEntity):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def act(self):
        """Define how a resident behaves each time step."""
        print(f"{self.name} is going about their daily activities.")
