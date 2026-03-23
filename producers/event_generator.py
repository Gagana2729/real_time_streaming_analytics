import json
import time
import random
from kafka import KafkaProducer

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

event_types = ["click", "purchase", "view"]

while True:
    event = {
        "event_id": str(random.randint(1000, 9999)),
        "user_id": f"user_{random.randint(1, 100)}",
        "event_type": random.choice(event_types),
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "page": "/home",
        "amount": round(random.uniform(10, 500), 2)
    }

    # Send to Kafka topic
    producer.send("user-events", value=event)

    print("Sent:", event)

    time.sleep(0.5)  # controls speed
>>>>>>> c44d5d015c4305ec24c2a5f1b6379938c6e5fba3
