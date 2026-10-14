from security import get_info


objects = ["laptop", "cell phone", "bottle", "cup", "person", "backpack"]

for obj in objects:
    info = get_info(obj)

    print("--------------------")
    print("Object:", obj)
    print("Status:", info["status"])
    print("Risk score:", info["risk_score"])
    print("Role:", info["role"])
    print("Description:", info["description"])