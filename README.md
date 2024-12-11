Here’s the updated `README.md` file for your project, including all the necessary details for setting up, configuring, and running the IntelliRescue AI framework:

---

# IntelliRescue AI Framework

The IntelliRescue AI Framework is an AI-driven emergency response system designed for vehicle crash scenarios. It leverages Fetch.ai agents for decentralized task handling, LangChain for orchestration and NLP capabilities, and a React-based dashboard for real-time visualization. This project was built as part of the Fetch.ai Hackathon to demonstrate how intelligent agents can improve emergency response times while preserving privacy.

---

## Features

1. **Crash Detection**: Identifies crashes using telemetry data (g-force, speed).
2. **Severity Analysis**: Evaluates crash severity based on road and weather conditions.
3. **Health Analysis**: Analyzes occupant health data.
4. **Responder Notification**: Sends crash details to emergency responders.
5. **Navigation**: Optimizes routes for emergency responders.
6. **Privacy-Preserving Multi-Agent System**: Utilizes Fetch.ai's multi-agent framework.
7. **Real-Time Dashboard**: Allows responders to monitor incidents and make decisions.

---

## Project Structure

```plaintext
IntelliRescue AI Framework/
├── agents/                          # Fetch.ai Agents
│   ├── CrashDetectionAgent/         # Detects crashes
│   ├── SeverityAnalysisAgent/       # Evaluates crash severity
│   ├── HealthAnalysisAgent/         # Analyzes occupant health
│   ├── ResponderNotificationAgent/  # Notifies responders
│   └── NavigationAgent/             # Optimizes responder routes
├── backend/                         # Backend for orchestration
│   ├── app.py                       # Main backend application
│   └── langchain_integration.py     # LangChain workflows
├── dashboard/                       # Real-Time Dashboard
│   └── src/
├── agent_addresses.json             # Centralized agent addresses and private keys
├── run_demo.py                      # Script to simulate workflows
├── tests/                           # Test suite for all components
├── documentation/                   # Documentation for the project
├── README.md                        # Project overview and setup guide
├── requirements.txt                 # Python dependencies
└── .env                             # Environment variables (API keys, etc.)
```

---

## Requirements

### 1. System Requirements
- Python 3.8 or higher
- Node.js (for the React dashboard)
- A Fetch.ai agent address and private key for each agent

### 2. API Keys Required
- **Google Maps API Key**: For navigation functionality.
- **Weather API Key**: For severity analysis (e.g., OpenWeatherMap).

---

## Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/intellirescue-ai.git
cd intellirescue-ai
```

### Step 2: Create and Activate a Virtual Environment
For Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
Install Python dependencies:
```bash
pip install -r requirements.txt
```

Install Node.js dependencies for the dashboard:
```bash
cd dashboard/src
npm install
cd ../../
```

### Step 4: Generate Agent Addresses
You’ll need to generate Fetch.ai agent addresses and private keys for each agent. You can use the Fetch.ai wallet or tools like `fetchcli` to generate keys.

Example:
```bash
fetchcli keys add <agent_name>
```

Store the generated `address` and `private_key` in the `agent_addresses.json` file:
```json
{
    "CrashDetectionAgent": {
        "address": "address_1",
        "private_key": "private_key_1"
    },
    "SeverityAnalysisAgent": {
        "address": "address_2",
        "private_key": "private_key_2"
    },
    "HealthAnalysisAgent": {
        "address": "address_3",
        "private_key": "private_key_3"
    },
    "ResponderNotificationAgent": {
        "address": "address_4",
        "private_key": "private_key_4"
    },
    "NavigationAgent": {
        "address": "address_5",
        "private_key": "private_key_5"
    }
}
```

### Step 5: Configure the `.env` File
Create a `.env` file in the root directory with the following content:
```plaintext
# General Configuration
AGENT_CONFIG_FILE=agent_addresses.json

# API Keys
MAPS_API_KEY=your_google_maps_api_key
WEATHER_API_KEY=your_weather_api_key

# Dashboard Configuration
DASHBOARD_HOST=127.0.0.1
DASHBOARD_PORT=8000

# Miscellaneous Settings
LOG_LEVEL=INFO
ENV=development
```

---

## Running the System

### 1. Start the Agents
Navigate to each agent directory and run the corresponding script. For example:
```bash
cd agents/CrashDetectionAgent
python agent.py
```
Repeat this for all agents (`CrashDetectionAgent`, `SeverityAnalysisAgent`, etc.).

### 2. Start the Backend
Run the backend application:
```bash
cd backend
python app.py
```

### 3. Start the Dashboard
Navigate to the dashboard directory and start the React server:
```bash
cd dashboard/src
npm start
```

### 4. Simulate Workflows
You can simulate a full workflow using the `run_demo.py` script:
```bash
python run_demo.py
```

---

## Testing

To run the test suite for all components:
```bash
pytest
```

---

## Usage

### Sending Telemetry Data to CrashDetectionAgent
Send a telemetry JSON object to the `CrashDetectionAgent`. Example:
```json
{
    "g_force": 5.2,
    "speed": 0,
    "timestamp": "2024-12-10T12:00:00Z",
    "location": {"latitude": 40.7128, "longitude": -74.0060}
}
```

Expected Response:
```json
{
    "crash_detected": true,
    "g_force": 5.2,
    "speed": 0,
    "timestamp": "2024-12-10T12:00:00Z",
    "location": {"latitude": 40.7128, "longitude": -74.0060}
}
```

---

## Notes

1. **Security**:
   - Add `agent_addresses.json` to `.gitignore` to avoid committing sensitive keys.
   - Use environment variables or a secure secrets manager in production.

2. **Extensibility**:
   - New agents can be added by defining them in `agents/` and updating `agent_addresses.json`.

3. **Troubleshooting**:
   - Ensure all dependencies are installed and environment variables are correctly set.
   - Use `LOG_LEVEL=DEBUG` for detailed logging.

---

## **Contributors**
- [Aman Gupta](https://github.com/amangupta05)

---

## License

This project is licensed under the MIT License.




---

