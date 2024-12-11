import json
import asyncio
from uagents import Agent
from uagents.models import Envelope
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

async def test_crash_detection_agent():
    # Load mock data
    with open("mock_data.json", "r") as f:
        mock_data = json.load(f)

    # Initialize the testing agent
    tester_agent = Agent(name="Tester", address="tester_address", private_key="tester_private_key")
    
    # Initialize the CrashDetectionAgent with address and private key from the config
    agent_config_file = os.getenv("AGENT_CONFIG_FILE", "agent_addresses.json")
    with open(agent_config_file, "r") as f:
        addresses = json.load(f)
    crash_detection_agent_address = addresses["CrashDetectionAgent"]["address"]

    # Define a response handler for the tester agent
    @tester_agent.on_event("response")
    async def handle_response(ctx, sender, message):
        print(f"Response from {sender}: {message}")

    # Start the tester agent
    tester_agent.run()

    # Send mock data to the CrashDetectionAgent
    for data in mock_data:
        envelope = Envelope(
            sender=tester_agent.address,
            target=crash_detection_agent_address,
            protocol="crash_proto",
            payload=data
        )
        print(f"Sending data: {data}")
        await tester_agent.send_envelope(envelope)

    # Allow time for responses
    await asyncio.sleep(5)

# Run the test
if __name__ == "__main__":
    asyncio.run(test_crash_detection_agent())
