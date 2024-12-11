

# IntelliRescue AI Framework

IntelliRescue is an AI-powered emergency response system designed to assist in vehicle crash scenarios. It leverages **Fetch.ai agents** for decentralized decision-making, **LangChain** for dynamic workflows and NLP capabilities, and a real-time **dashboard** for emergency responders. This project is built for the Fetch.ai Hackathon and demonstrates a seamless integration of AI technologies to solve real-world challenges.

---

## **Features**
- **Crash Detection**: Monitors vehicle telemetry and identifies crash events using Fetch.ai agents.
- **Severity Analysis**: Evaluates crash severity based on impact data and environmental conditions.
- **Health Analysis**: Analyzes occupant vitals to assess medical urgency.
- **Responder Notification**: Sends secure, real-time alerts to emergency responders.
- **Route Optimization**: Provides responders with the best route to the crash site.
- **NLP Integration**: Uses LangChain for natural language guidance to occupants and workflow orchestration.
- **Real-Time Dashboard**: Visualizes crash details, responder updates, and incident logs.

---

## **Project Structure**

```plaintext
IntelliRescue_AI_Framework/
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
├── run_demo.py                      # Script to automate workflows
├── tests/                           # Test suite for all components
├── documentation/                   # Documentation for the project
├── README.md                        # Project overview and setup guide
├── requirements.txt                 # Python dependencies
└── .env                             # Environment variables
```

---

## **Installation**

### **Prerequisites**
1. Python 3.9 or higher
2. Node.js and npm
3. Virtual Environment (optional)

### **Clone the Repository**
```bash
git clone https://github.com/amangupta05/IntelliRescue-AI-Framework.git
cd IntelliRescue-AI-Framework
```

---

## **Setup**

### **Backend**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment variables:
   - Create a `.env` file in the root directory:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     MAPS_API_KEY=your_maps_api_key
     ```
3. Start the backend server:
   ```bash
   python backend/app.py
   ```

### **Agents**
Start each agent in a separate terminal window:
```bash
python agents/CrashDetectionAgent/agent.py
python agents/SeverityAnalysisAgent/agent.py
python agents/HealthAnalysisAgent/agent.py
python agents/ResponderNotificationAgent/agent.py
python agents/NavigationAgent/agent.py
```

### **Dashboard**
1. Navigate to the dashboard directory:
   ```bash
   cd dashboard
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the dashboard:
   ```bash
   npm start
   ```

---

## **Demo**
1. Run the centralized demo script:
   ```bash
   python run_demo.py
   ```
2. View real-time updates on the dashboard at:
   ```plaintext
   http://localhost:3000
   ```

---

## **Technologies Used**
- **Fetch.ai**: Decentralized agents for crash detection, analysis, and responder notification.
- **LangChain**: Workflow orchestration and NLP for guidance and summarization.
- **React**: Frontend dashboard for visualizing crash details and responder updates.
- **SQLite**: Database for logging crash incidents and analytics.

---

## **Hackathon Highlights**
- Fully automated workflow with preloaded mock data.
- Real-time dashboard for responder visualization.
- Privacy-preserving data handling with Fetch.ai enclaves.
- Scalable and modular architecture for future enhancements.

---

## **Future Improvements**
- Integrate live IoT sensor data.
- Add real-time responder tracking on the map.
- Enhance NLP models for more personalized guidance.

---

## **Contributors**
- [Aman Gupta](https://github.com/amangupta05)


---

