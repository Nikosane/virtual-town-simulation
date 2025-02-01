import random

class EventManager:
    def __init__(self):
        self.events = [
            "Rainstorm",
            "Economic Boom",
            "Power Outage",
            "Festival",
            "Market Crash"
        ]
    
    def trigger_event(self):
        """Randomly selects an event and returns it."""
        event = random.choice(self.events)
        print(f"Event Triggered: {event}")
        return event
