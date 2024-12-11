import os
import json
from uagents import Agent, Context, Model, Protocol
from dotenv import load_dotenv
import logging
# Load environment variables
load_dotenv()

# Define message structures
class TelemetryData(Model):
    g_force: float
    speed: float
    timestamp: str
    location: dict

class CrashDetectionResponse(Model):
    crash_detected: bool
    g_force: float = 0.0
    speed: float = 0.0
    timestamp: str = ""
    location: dict = {}

# Define the crash detection protocol
crash_proto = Protocol()

@crash_proto.on_message(model=TelemetryData, replies={CrashDetectionResponse})
async def handle_telemetry_data(ctx: Context, sender: str, msg: TelemetryData):
    """
    Handle incoming telemetry data and determine if a crash has occurred.
    """
    try:
        g_force = msg.g_force
        speed = msg.speed
        crash_detected = g_force > 3.0 or speed == 0  # Example crash detection thresholds

        # Formulate response
        response = CrashDetectionResponse(
            crash_detected=crash_detected,
            g_force=g_force,
            speed=speed,
            timestamp=msg.timestamp,
            location=msg.location,
        )
        await ctx.send(sender, response)
    except Exception as e:
        ctx.logger.error(f"Error processing telemetry data: {str(e)}")

# Define the CrashDetectionAgent class
class CrashDetectionAgent:
    def __init__(self, agent_name: str):
        """
        Initialize the CrashDetectionAgent with address and private key loaded from agent_addresses.json.
        """
        # Load agent address and private key from centralized configuration file
        print("Hello")
        # agent_config_file = os.getenv("AGENT_CONFIG_FILE")

        # with open("D:\projects\Fetch.ai Hackathon\IntelliRescue-AI-Framework\agent_addresses.json", "r") as f:
        addresses = {
            "CrashDetectionAgent": {
            "address": "agent1qdjdfquw7ud0kh6fhl3ewle8kr0kmlgf297zyknz5k6jmfnvdl907kcx8zc",
            "private_key": "73224ebf70ad8e3635b7cbe462a7176e7f89b4eaee1ed439de2a39260b596432"
            },
            "SeverityAnalysisAgent": {
            "address": "agent1qg5ukhkd3zzfeaxhetdmn3w3n27ck38mk7x360h5x0r02u9aj7sfq26adt4",
            "private_key": "000e270d3a2e9f49aee284f84f74e8391314dc052d39f1f18553f68236ccbde3"
            },
            "HealthAnalysisAgent": {
            "address": "agent1qtzaexsp4wu7gqenhhfvh6v2zrekqtkdx8kh597l7rtlhz4ewcu7q89vk0u",
            "private_key": "07b084e43eb28b2591eda4e81588d5377e3c69268bb3c441a5e0e04af37564fd"
            },
            "ResponderNotificationAgent": {
            "address": "agent1q23n57638u76c5vstrgdqt7u8uekyym8qj7emc2mveu59azh4le7jp0mrd3",
            "private_key": "999452024c02a7ef08d165ef605befc31049947b066530613d6234e46c7d88c7"
            },
            "NavigationAgent": {
            "address": "agent1q26hdm66jfnh69gg2mgcpx6aeanqjusvvla97e9t0dv2a7vap9x8cjz9a4m",
            "private_key": "403a8d732ce118ea95d089b0b3c0ea6f8594dcd3f26233e481dc417430a48332"
            }
        }
        # addresses = json.load(f)

        if agent_name not in addresses:
            raise ValueError(f"Agent name '{agent_name}' not found in {agent_config_file}.")


        agent_info = addresses[agent_name]
        self.agent_name = agent_name
        self.address = agent_info["address"]
        self.private_key = agent_info["private_key"]

        # Initialize the agent with supported parameters
        self.agent = Agent(
            name=agent_name,
            seed=self.private_key,
            enable_agent_inspector=True,  # Enable agent inspector for debugging
            log_level=logging.INFO,
            endpoint="http://127.0.0.1:8000"
        )
        self.agent.include(crash_proto)

        print(f"{agent_name} initialized with address: {self.address}")
        
        # Add REST handler for the root endpoint
        @self.agent.on_rest_get("/", response=CrashDetectionResponse)
        async def root_handler(_ctx: Context):
            return {"message": "Welcome to CrashDetectionAgent"}

        print(f"{self.agent_name} initialized with address: {self.address}")
    def run(self):
        """ 
        Run the CrashDetectionAgent.
        """
        print(f"Starting {self.agent_name}...")
        self.agent.run()

# Main entry point
if __name__ == "__main__":
    try:
        crash_detection_agent = CrashDetectionAgent(agent_name="CrashDetectionAgent")
        crash_detection_agent.run()
    except Exception as e:
        print(f"Error starting CrashDetectionAgent: {e}")
# import os
# import json
# from fetchai.crypto import Identity
# from fetchai.communication import send_message_to_agent, parse_message_from_agent
# from fetchai.registration import register_with_agentverse
# from fetchai import fetch
# from uagents import Agent, Context, Model, Protocol
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Define message structures using FetchAI's Model
# class TelemetryData(Model):
#     g_force: float
#     speed: float
#     timestamp: str
#     location: dict

# class CrashDetectionResponse(Model):
#     crash_detected: bool
#     g_force: float = 0.0
#     speed: float = 0.0
#     timestamp: str = ""
#     location: dict = {}

# # Define the crash detection protocol
# crash_proto = Protocol()

# @crash_proto.on_message(model=TelemetryData, replies={CrashDetectionResponse})
# async def handle_telemetry_data(ctx: Context, sender: str, msg: TelemetryData):
#     """
#     Handle incoming telemetry data and determine if a crash has occurred.
#     """
#     try:
#         g_force = msg.g_force
#         speed = msg.speed
#         crash_detected = g_force > 3.0 or speed == 0  # Example crash thresholds

#         # Formulate response
#         response = CrashDetectionResponse(
#             crash_detected=crash_detected,
#             g_force=g_force,
#             speed=speed,
#             timestamp=msg.timestamp,
#             location=msg.location,
#         )
#         await ctx.send(sender, response)
#     except Exception as e:
#         ctx.logger.error(f"Error processing telemetry data: {str(e)}")

# # Register the AI with AgentVerse
# def register_crash_detection_ai():
#     """
#     Register the CrashDetectionAgent with AgentVerse for discoverability.
#     """
#     AGENTVERSE_KEY = os.getenv("AGENTVERSE_KEY")
#     AI_KEY = os.getenv("AI_KEY")

#     ai_identity = Identity.from_seed(AI_KEY, 0)

#     # AI metadata
#     name = "CrashDetectionAgent"
#     readme = """
#     <description>An AI agent that detects crashes based on telemetry data such as g-force and speed.</description>
#     <use_cases>
#         <use_case>Real-time crash detection for vehicles.</use_case>
#     </use_cases>
#     <payload_requirements>
#         <description>
#             Provide telemetry data for crash analysis.
#         </description>
#         <payload>
#             <requirement>
#                 <parameter>g_force</parameter>
#                 <description>Measured g-force of the vehicle.</description>
#             </requirement>
#             <requirement>
#                 <parameter>speed</parameter>
#                 <description>Current speed of the vehicle.</description>
#             </requirement>
#             <requirement>
#                 <parameter>timestamp</parameter>
#                 <description>Timestamp of the telemetry data.</description>
#             </requirement>
#             <requirement>
#                 <parameter>location</parameter>
#                 <description>Geographical location of the vehicle.</description>
#             </requirement>
#         </payload>
#     </payload_requirements>
#     """
#     ai_webhook = os.getenv("AI_WEBHOOK")

#     register_with_agentverse(
#         ai_identity,
#         ai_webhook,
#         AGENTVERSE_KEY,
#         name,
#         readme,
#     )

# # Define the CrashDetectionAgent
# class CrashDetectionAgent:
#     def __init__(self):
#         """
#         Initialize the CrashDetectionAgent and include the crash detection protocol.
#         """
#         AI_KEY = os.getenv("AI_KEY")
#         self.identity = Identity.from_seed(AI_KEY, 0)
#         self.agent = Agent(name="CrashDetectionAgent", address=self.identity.address, private_key=self.identity.private_key)
#         self.agent.include(crash_proto)

#     def run(self):
#         """
#         Run the agent.
#         """
#         print(f"CrashDetectionAgent running at address: {self.agent.address}")
#         self.agent.run()

# # Test the agent with mock data
# async def test_agent_with_mock_data():
#     """
#     Simulate sending telemetry data to the CrashDetectionAgent.
#     """
#     AI_KEY = os.getenv("AI_KEY")
#     identity = Identity.from_seed(AI_KEY, 0)

#     # Sample telemetry data
#     telemetry_data = [
#         {"g_force": 4.5, "speed": 0, "timestamp": "2024-12-10T12:00:00Z", "location": {"latitude": 40.7128, "longitude": -74.0060}},
#         {"g_force": 1.2, "speed": 50, "timestamp": "2024-12-10T12:10:00Z", "location": {"latitude": 34.0522, "longitude": -118.2437}},
#     ]

#     # Fetch the CrashDetectionAgent's address
#     available_ais = fetch.ai("Crash Detection")
#     agent_address = available_ais.get("ais")[0]["address"]

#     for data in telemetry_data:
#         response = send_message_to_agent(identity, agent_address, data)
#         print(f"Sent: {data}")
#         print(f"Response: {response}")

# # Main entry point
# if __name__ == "__main__":
#     try:
#         register_crash_detection_ai()  # Register the agent with AgentVerse
#         crash_detection_agent = CrashDetectionAgent()
#         crash_detection_agent.run()  # Start the agent
#     except Exception as e:
#         print(f"Error starting CrashDetectionAgent: {e}")
