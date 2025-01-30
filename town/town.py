class Town:
    def __init__(self, clock):
        self.clock = clock
        self.residents = []  # List of resident entities
        self.businesses = []  # List of business entities
        print(f"{self.__class__.__name__} initialized.")
    
    def update(self):
        """Update the town state for the current time step."""
        print(f"Updating {self.__class__.__name__} for time {self.clock.current_time}")
        for resident in self.residents:
            resident.act()
        for business in self.businesses:
            business.operate()
    
    def add_resident(self, resident):
        self.residents.append(resident)
    
    def add_business(self, business):
        self.businesses.append(business)
