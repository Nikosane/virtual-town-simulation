import requests
import config

class LLMConnector:
    def __init__(self):
        self.api_key = config.LLM_API_KEY
        self.api_url = "https://api.example.com/llm"  # Replace with actual API endpoint
        
    def get_decision(self, prompt):
        """Send a prompt to the LLM and return the response."""
        response = requests.post(
            self.api_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"prompt": prompt}
        )
        
        if response.status_code == 200:
            return response.json().get("response", "No response")
        else:
            print("Error in LLM API call:", response.text)
            return "Error"
