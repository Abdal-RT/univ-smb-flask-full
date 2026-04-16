from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def load_data(filename):
    with open(os.path.join(DATA_DIR, filename), 'r') as f:
        return json.load(f)

def save_data(filename, data):
    with open(os.path.join(DATA_DIR, filename), 'w') as f:
        json.dump(data, f, indent=2)

# ───── Routes de base ─────
@app.route("/")
def hello():
    return "Hello, API!"

# ───── LOAD BALANCER ─────
@app.route("/config/lb", methods=["GET"])
def get_all_lb():
    return jsonify(load_data("loadbalancer.json"))

@app.route("/config/lb/<int:id>", methods=["GET"])
def get_lb(id):
    items = load_data("loadbalancer.json")
    item = next((x for x in items if x["id"] == id), None)
    if item is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item)

@app.route("/config/lb", methods=["POST"])
def create_lb():
    items = load_data("loadbalancer.json")
    new_item = request.get_json()
    new_item["id"] = max((x["id"] for x in items), default=0) + 1
    items.append(new_item)
    save_data("loadbalancer.json", items)
    return jsonify(new_item), 201

@app.route("/config/lb/<int:id>", methods=["DELETE"])
def delete_lb(id):
    items = load_data("loadbalancer.json")
    items = [x for x in items if x["id"] != id]
    save_data("loadbalancer.json", items)
    return jsonify({"message": "Deleted"}), 200

# ───── REVERSE PROXY ─────
@app.route("/config/rp", methods=["GET"])
def get_all_rp():
    return jsonify(load_data("reverseproxy.json"))

@app.route("/config/rp/<int:id>", methods=["GET"])
def get_rp(id):
    items = load_data("reverseproxy.json")
    item = next((x for x in items if x["id"] == id), None)
    if item is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item)

@app.route("/config/rp", methods=["POST"])
def create_rp():
    items = load_data("reverseproxy.json")
    new_item = request.get_json()
    new_item["id"] = max((x["id"] for x in items), default=0) + 1
    items.append(new_item)
    save_data("reverseproxy.json", items)
    return jsonify(new_item), 201

@app.route("/config/rp/<int:id>", methods=["DELETE"])
def delete_rp(id):
    items = load_data("reverseproxy.json")
    items = [x for x in items if x["id"] != id]
    save_data("reverseproxy.json", items)
    return jsonify({"message": "Deleted"}), 200

# ───── WEB SERVER ─────
@app.route("/config/ws", methods=["GET"])
def get_all_ws():
    return jsonify(load_data("webserver.json"))

@app.route("/config/ws/<int:id>", methods=["GET"])
def get_ws(id):
    items = load_data("webserver.json")
    item = next((x for x in items if x["id"] == id), None)
    if item is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(item)

@app.route("/config/ws", methods=["POST"])
def create_ws():
    items = load_data("webserver.json")
    new_item = request.get_json()
    new_item["id"] = max((x["id"] for x in items), default=0) + 1
    items.append(new_item)
    save_data("webserver.json", items)
    return jsonify(new_item), 201

@app.route("/config/ws/<int:id>", methods=["DELETE"])
def delete_ws(id):
    items = load_data("webserver.json")
    items = [x for x in items if x["id"] != id]
    save_data("webserver.json", items)
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)