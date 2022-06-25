import json

import requests

response = requests.get(
    "http://127.0.0.1:5000/gap_text",
)

print("Raw:\n" + response.text)
print("Formatted:\n" + json.dumps(json.loads(response.text), indent=4))