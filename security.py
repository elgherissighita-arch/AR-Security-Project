import json

# Load security data
with open("security_data.json", "r") as file:
    security_data = json.load(file)


def get_info(name):
    return security_data.get(
        name,
        {
            "role": "unknown",
            "risk_score": 0,
            "status": "Unknown",
            "description": "No security information available"
        }
    )