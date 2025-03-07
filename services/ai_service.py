import requests
import time
from utils.error_handling import APIError


class AIService:
    API_URL = "https://api.mistral.ai/v1/chat/completions"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _make_request(self, prompt: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "open-mistral-7b",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500,
            "temperature": 0.3,
        }
        try:
            response = requests.post(self.API_URL, headers=headers, json=payload)
            response_json = response.json()
            return self._parse_response(response_json, prompt)
        except requests.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")

    def _parse_response(self, response_json: dict, prompt: str):
        if "error" in response_json:
            raise APIError(f"API Error: {response_json['error']}")
        if (
            "message" in response_json
            and "Requests rate limit exceeded" in response_json["message"]
        ):
            print("Rate limit hit, retrying in 5 seconds...")
            time.sleep(5)
            return self._make_request(prompt)
        if "choices" in response_json and response_json["choices"]:
            return response_json["choices"][0]["message"]["content"].strip()
        raise APIError("Unexpected API response format")

    def get_ai_feedback(self, prompt: str):
        try:
            return self._make_request(prompt) or "No response received from API."
        except APIError as e:
            return str(e)
