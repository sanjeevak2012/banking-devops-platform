from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/transaction")
def transaction():
    return jsonify(
        transaction_id="TXN123",
        amount=50000,
        status="SUCCESS"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

@app.route("/transaction", methods=["POST"])
def create_transaction():
    event = {
        "event": "transaction-created",
        "amount": 100,
        "currency": "INR"
    }

    producer.send("transactions", event)

    return jsonify({"status": "transaction event published"}), 201


@app.route("/health")
def health():
    return jsonify({"status": "UP"})
from flask import Flask, jsonify
from kafka import KafkaProducer
from flask import Flask, jsonify, request

@app.route("/transaction", methods=["POST"])
def transaction():
    event = {
        "transaction_id": "TXN123",
        "amount": 50000,
        "status": "SUCCESS"
    }

    producer.send("transactions", event)

    return jsonify(event)
