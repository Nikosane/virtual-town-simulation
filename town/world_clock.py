class WorldClock:
    def __init__(self, start_time=0):
        self.current_time = start_time
        print(f"WorldClock initialized at time {self.current_time}")
    
    def tick(self, step=1):
        """Advance the world clock by a given time step."""
        self.current_time += step
        print(f"World time advanced to {self.current_time}")
