import logging

# Configure logging
logging.basicConfig(
    filename="simulation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_event(message):
    """Logs an event in the simulation."""
    logging.info(message)
    print(message)
