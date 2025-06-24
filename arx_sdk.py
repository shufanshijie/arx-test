import requests

class ArxServiceClient:
    """
    A client for interacting with the ARX Service API.
    """
    def __init__(self, base_url="http://localhost:8080"):
        """
        Initializes the API client.
        Args:
            base_url (str): The base URL of the ARX service.
                          Defaults to "http://localhost:8080".
        """
        self.base_url = base_url

    def get_hello(self):
        """
        Calls the /api/hello endpoint.
        Returns:
            dict: The JSON response from the API, or None if an error occurs.
        """
        try:
            response = requests.get(f"{self.base_url}/api/hello")
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while calling the hello API: {e}")
            return None

    def get_health(self):
        """
        Calls the /api/health endpoint.
        Returns:
            dict: The JSON response from the API, or None if an error occurs.
        """
        try:
            response = requests.get(f"{self.base_url}/api/health")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while calling the health API: {e}")
            return None

    def is_service_healthy(self) -> bool:
        """
        Checks if the service is healthy by calling the health endpoint.
        Returns:
            bool: True if the service status is 'UP', False otherwise.
        """
        health_data = self.get_health()
        if health_data and health_data.get("status") == "UP":
            return True
        return False 