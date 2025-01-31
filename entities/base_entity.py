class BaseEntity:
    def __init__(self, name):
        self.name = name
        print(f"{self.__class__.__name__} '{self.name}' initialized.")
    
    def act(self):
        """Define the basic action of an entity. Should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")
