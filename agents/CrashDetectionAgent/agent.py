import json
from uagents import Agent, Context, Model, Protocol
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Define message structures using Models
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
        # Extract telemetry data
        g_force = msg.g_force
        speed = msg.speed

        # Simplistic crash detection logic
        crash_detected = g_force > 3.0 or speed == 0  # Example thresholds

        # Create a response
        response = CrashDetectionResponse(
            crash_detected=crash_detected,
            g_force=g_force,
            speed=speed,
            timestamp=msg.timestamp,
            location=msg.location,
        )

        # Send the response
        await ctx.send(sender, response)
    except Exception as e:
        ctx.logger.error(f"Error processing telemetry data: {str(e)}")

# Define the CrashDetectionAgent class
class CrashDetectionAgent:
    def __init__(self, agent_name: str):
        """
        Initialize the CrashDetectionAgent with address and private key.
        """
        # Load agent address and private key from centralized config
        agent_config_file = os.getenv("AGENT_CONFIG_FILE", "agent_addresses.json")
        with open(agent_config_file, "r") as f:
            addresses = json.load(f)

        if agent_name not in addresses:
            raise ValueError(f"Agent name '{agent_name}' not found in {agent_config_file}.")

        agent_info = addresses[agent_name]
        self.agent = Agent(name=agent_name, address=agent_info["address"], private_key=agent_info["private_key"])
        self.agent_name = agent_name

        # Include the crash detection protocol
        self.agent.include(crash_proto)

    def run(self):
        """
        Run the agent.
        """
        print(f"{self.agent_name} is running with address: {self.agent.address}")
        self.agent.run()

# Instantiate and run the CrashDetectionAgent
if __name__ == "__main__":
    try:
        crash_detection_agent = CrashDetectionAgent(agent_name="CrashDetectionAgent")
        crash_detection_agent.run()
    except Exception as e:
        print(f"Failed to start CrashDetectionAgent: {e}")
