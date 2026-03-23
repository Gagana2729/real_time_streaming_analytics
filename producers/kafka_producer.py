from kafka import KafkaProducer
import json
import time
import random
import uuid
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC = "streaming-data"

print("Producer started...")

while True:
    event = {
        "event_id": str(uuid.uuid4()),
        "user_id": f"u_{random.randint(1000,9999)}",
        "event_type": random.choice(["click","view","purchase"]),
        "timestamp": datetime.utcnow().isoformat(),
        "page": random.choice(["/home","/product","/checkout"]),
        "amount": round(random.uniform(10,500),2),
        "session_id": f"s_{random.randint(1000,9999)}",
        "device": random.choice(["mobile","desktop"])
    }

    producer.send(TOPIC, event)
    print("sent:", event)

    time.sleep(1)