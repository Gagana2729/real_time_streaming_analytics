import json
import random
import uuid
import time
from datetime import datetime

EVENT_TYPES = ["click", "view", "purchase", "error"]
PAGES = ["/home", "/product", "/checkout", "/search"]
DEVICES = ["mobile", "desktop"]

def generate_event():
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": f"u_{random.randint(1000,9999)}",
        "event_type": random.choice(EVENT_TYPES),
        "timestamp": datetime.utcnow().isoformat(),
        "page": random.choice(PAGES),
        "amount": round(random.uniform(10, 500), 2),
        "session_id": f"s_{random.randint(10000,99999)}",
        "device": random.choice(DEVICES)
    }

if __name__ == "__main__":
    while True:
        event = generate_event()
        print(json.dumps(event))
        time.sleep(0.01)