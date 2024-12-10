# IntelliRescue AI Framework

## Overview
The **IntelliRescue AI Framework** is a cutting-edge, AI-driven emergency response system designed to detect, analyze, and respond to critical situations like vehicle crashes. By leveraging Fetch.ai’s decentralized agent framework, LangChain’s intelligent workflow orchestration, and privacy-focused data handling, this project ensures optimized response times and secure communication with emergency services.

---

## Features
- **Real-Time Crash Detection**: Monitors IoT telemetry to identify crash events instantaneously.
- **Severity and Health Analysis**: Evaluates crash severity and occupant health for triaging responders.
- **Optimized Routing**: Provides real-time navigation for emergency services to minimize response times.
- **Privacy-Preserving Data Sharing**: Secures sensitive data using Fetch.ai’s enclave technology.
- **Interactive Dashboard**: Displays critical incident details and visualizations for emergency teams.

---

## Project Structure
```
IntelliRescue AI Framework
├── agents
│   ├── CrashDetectionAgent
│   │   └── agent.py
│   ├── SeverityAnalysisAgent
│   │   └── agent.py
│   ├── HealthAnalysisAgent
│   │   └── agent.py
│   ├── ResponderNotificationAgent
│   │   └── agent.py
│   └── NavigationAgent
│       └── agent.py
├── backend
│   ├── app.py
│   └── langchain_integration.py
├── dashboard
│   └── App.js
├── documentation
│   └── AI-Driven_Emergency_Response_System_Documentation.docx
└── README.md
```

---

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Node.js 14+
- Flask
- Fetch.ai SDK
- LangChain
- React.js

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/IntelliRescue-AI.git
   cd IntelliRescue-AI
   ```

2. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install frontend dependencies:
   ```bash
   cd dashboard
   npm install
   ```

4. Start the backend server:
   ```bash
   python backend/app.py
   ```

5. Start the frontend:
   ```bash
   cd dashboard
   npm start
   ```

---

## Usage
1. Simulate crash data using the provided `simulate_data.py` script (found in `backend`).
2. Use the dashboard to visualize real-time crash detections, severity levels, and responder routes.
3. Test agent interactions via the LangChain integration in `langchain_integration.py`.

---

## How It Works

### Agents and Orchestration
- **Crash Detection Agent**: Detects crash events based on IoT sensor data.
- **Severity Analysis Agent**: Assesses crash severity using telemetry and weather data.
- **Health Analysis Agent**: Analyzes occupant vitals to prioritize medical needs.
- **Responder Notification Agent**: Securely shares crash details with responders.
- **Navigation Agent**: Calculates optimal routes for emergency vehicles.

### LangChain
The LangChain orchestrator manages workflows between agents and communicates with the frontend for real-time updates.

---

## Contributing
We welcome contributions to the **IntelliRescue AI Framework**. To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add YourFeatureName"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For inquiries, please reach out to:
- **Name:** Aman Gupta
- **Email:** amangupta52001@gmail.com

---


