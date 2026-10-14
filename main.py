
from security import get_info, check_object

objects = ["laptop", "cell phone", "bottle", "cup", "person", "backpack"]

for obj in objects:
    info = get_info(obj)

    print("--------------------")
    print("Object:", obj)
    print("Status:", info["status"])
    print("Risk score:", info["risk_score"])
    print("Role:", info["role"])
    print("Description:", info["description"])


print("\n--- Integration test ---")

detected_object = {
    "name": "cell phone",
    "confidence": 0.92
}

result = check_object(detected_object)

print(result)
