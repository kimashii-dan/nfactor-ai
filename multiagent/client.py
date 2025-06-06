import requests

# Replace with your actual base URL if hosted elsewhere
BASE_URL = "http://localhost:8000"

# Step 1: Send a text to analyzer
text_input = "The Eiffel Tower is in Paris."

response = requests.post(f"{BASE_URL}/analyze", json={"text": text_input})

if response.ok:
    print("Final Result:", response.json())
else:
    print("Error:", response.status_code, response.text)