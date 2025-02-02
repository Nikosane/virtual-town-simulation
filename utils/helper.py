import random

def get_random_name():
    """Generate a random name for an entity."""
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    return random.choice(names)

def get_random_age(min_age=18, max_age=80):
    """Generate a random age within a given range."""
    return random.randint(min_age, max_age)
