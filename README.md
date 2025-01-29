# Virtual Town Simulation

## Overview
This project is a virtual simulation of a small town where AI-driven entities (residents and businesses) make their own decisions using an LLM (Large Language Model) API. The town evolves dynamically based on entity interactions, events, and decision-making processes.

## Features
- **AI-Driven Entities**: Residents and businesses interact with each other and take actions based on LLM-generated responses.
- **Dynamic Town Environment**: A time-based simulation where events unfold over time.
- **LLM Integration**: Entities communicate with an LLM API to determine their actions.
- **Event System**: Random or scripted events (e.g., weather changes, economic shifts) influence the town.
- **Logging and State Management**: Tracks the simulation's progress and interactions.

## Project Structure
```
virtual_town_simulation/
│── main.py                     # Entry point for running the simulation
│── config.py                   # Configuration settings (API keys, town parameters)
│── town/
│   │── town.py                 # Main simulation environment
│   │── world_clock.py           # Manages time progression
│── entities/
│   │── base_entity.py           # Base class for all entities
│   │── resident.py              # AI-driven residents
│   │── business.py              # AI-driven businesses
│── ai/
│   │── llm_connector.py         # Handles API calls to LLM
│── events/
│   │── event_manager.py         # Manages dynamic events
│── utils/
│   │── logger.py                # Handles logging
│   │── helper.py                # General utility functions
│── data/
│   │── town_state.json          # Stores the current town state (optional)
│── README.md                    # Project documentation
│── requirements.txt              # Dependencies
```

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/virtual_town_simulation.git
   cd virtual_town_simulation
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys:**
   - Edit `config.py` and add your LLM API key.

4. **Run the Simulation:**
   ```bash
   python main.py
   ```

## How It Works
- The simulation initializes a town with residents and businesses.
- Entities request decisions from the LLM API (e.g., "What should I do today?").
- The event system introduces dynamic changes.
- Logs capture interactions and decisions for debugging.

## Future Enhancements
- **More entity types** (e.g., government, schools, transport systems).
- **Advanced decision-making** (memory-based behaviors, evolving strategies).
- **Better visualization** (web UI or graphical representation of the town).

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request!

## License
This project is open-source and available under the MIT License.


