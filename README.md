# Virtual Town Simulation

## Overview
This project is a virtual simulation of a small town where AI-driven entities (residents and businesses) make their own decisions using an LLM (Large Language Model) API. The town evolves dynamically based on entity interactions, events, and decision-making processes.

## Features
- **AI-Driven Entities**: Residents and businesses interact with each other and take actions based on LLM-generated responses.
- **Dynamic Town Environment**: A time-based simulation where events unfold over time.
- **LLM Integration**: Entities communicate with an LLM API to determine their actions.
- **Event System**: Random or scripted events (e.g., weather changes, economic shifts) influence the town.
- **Logging and State Management**: Tracks the simulation's progress and interactions.


## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Nikosane/virtual_town_simulation.git
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


