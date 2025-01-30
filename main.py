import config
from town.town import Town
from town.world_clock import WorldClock

def main():
    print("Starting Virtual Town Simulation...")
    
    # Initialize simulation components
    clock = WorldClock()
    town = Town(clock)
    
    # Run the simulation loop
    while True:
        town.update()
        clock.tick()
        
        if clock.current_time > config.SIMULATION_END_TIME:
            print("Simulation ended.")
            break

if __name__ == "__main__":
    main()
