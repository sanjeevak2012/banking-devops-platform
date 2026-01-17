import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="kafka:9092",
    group_id="audit-service",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Audit service started. Waiting for messages...")

for message in consumer:
    print("AUDIT LOG:", message.value)
