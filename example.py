from arx_sdk import ArxServiceClient

def main():
    """
    An example of how to use the ArxServiceClient.
    """
    print("--- Initializing ARX Service Client ---")
    client = ArxServiceClient()

    # --- 1. Check if the service is healthy ---
    print("\n1. Checking service health...")
    if client.is_service_healthy():
        print("✅ Service is UP and running.")
    else:
        print("❌ Service is down or not responding correctly.")
        return # Exit if service is not healthy

    # --- 2. Call the 'hello' endpoint ---
    print("\n2. Calling the 'hello' endpoint...")
    hello_response = client.get_hello()
    if hello_response:
        print("Response from /api/hello:")
        print(f"  Message: {hello_response.get('message')}")
        print(f"  Status: {hello_response.get('status')}")
        print(f"  Timestamp: {hello_response.get('timestamp')}")

    # --- 3. Call the 'health' endpoint again to show full details ---
    print("\n3. Calling the 'health' endpoint for details...")
    health_response = client.get_health()
    if health_response:
        print("Response from /api/health:")
        print(f"  Service Name: {health_response.get('service')}")
        print(f"  Status: {health_response.get('status')}")
        print(f"  Timestamp: {health_response.get('timestamp')}")

if __name__ == "__main__":
    main() 