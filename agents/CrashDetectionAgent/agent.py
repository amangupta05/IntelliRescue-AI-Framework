import json
from uagents.resolver import DNSResolver
from uagents.protocol.default import DefaultMessage
from uagents.agent import Agent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class CrashDetectionAgent(Agent):
    def __init__(self, agent_name: str):
        """
        Initialize the CrashDetectionAgent.
        """
        # Load agent address and private key from centralized config
        agent_config_file = os.getenv("AGENT_CONFIG_FILE", "agent_addresses.json")
        with open(agent_config_file, "r") as f:
            addresses = json.load(f)

        if agent_name not in addresses:
            raise ValueError(f"Agent name '{agent_name}' not found in {agent_config_file}.")

        agent_info = addresses[agent_name]
        super().__init__(agent_info["address"], agent_info["private_key"])
        self.agent_name = agent_name
        print(f"{agent_name} initialized with address: {agent_info['address']}")

    def detect_crash(self, telemetry_data):
        """
        Analyze telemetry data to detect crashes.

        Args:
            telemetry_data (dict): Dictionary containing telemetry data such as g-force, speed, etc.

        Returns:
            dict: Crash details if a crash is detected, else a message indicating no crash.
        """
        try:
            g_force = telemetry_data.get("g_force", 0)
            speed = telemetry_data.get("speed", 0)

            # Crash detection logic
            if g_force > 3.0 or speed == 0:  # Example thresholds for crash detection
                return {
                    "crash_detected": True,
                    "g_force": g_force,
                    "speed": speed,
                    "timestamp": telemetry_data.get("timestamp"),
                    "location": telemetry_data.get("location"),
                }
            return {"crash_detected": False}
        except Exception as e:
            return {"error": f"Crash detection failed: {str(e)}"}

    async def handle_message(self, envelope):
        """
        Handles incoming messages with telemetry data.

        Args:
            envelope: Incoming message envelope.
        """
        message = DefaultMessage.decode(envelope.message)
        if message.performative == DefaultMessage.Performative.REQUEST:
            try:
                telemetry_data = json.loads(message.content)
                crash_details = self.detect_crash(telemetry_data)
                response = DefaultMessage(
                    performative=DefaultMessage.Performative.INFORM,
                    content=json.dumps(crash_details),
                )
                await self.send(envelope.sender, response)
            except Exception as e:
                error_response = DefaultMessage(
                    performative=DefaultMessage.Performative.ERROR,
                    content=json.dumps({"error": str(e)}),
                )
                await self.send(envelope.sender, error_response)

# Instantiate and run the CrashDetectionAgent
if __name__ == "__main__":
    try:
        crash_detection_agent = CrashDetectionAgent(agent_name="CrashDetectionAgent")
        crash_detection_agent.run()
    except Exception as e:
        print(f"Failed to start CrashDetectionAgent: {e}")
