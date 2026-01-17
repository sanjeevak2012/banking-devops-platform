from flask import Flask, jsonify, request
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/transaction", methods=["POST"])
def transaction():
    event = {
        "transaction_id": "TXN123",
        "amount": 50000,
        "status": "SUCCESS"
    }

    producer.send("transactions", event)
    producer.flush()

    return jsonify({
        "message": "Transaction event published",
        "event": event
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
