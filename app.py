from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, REGISTRY

app = Flask(__name__)

# Create a Prometheus counter
REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@app.route('/data')
def get_data():
    REQUEST_COUNT.inc()
    return jsonify({"message": "Hello World"})

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}

# Liveness probe endpoint
@app.route('/healthz')
def healthz():
    return jsonify(status="ok"), 200

# Readiness probe endpoint
@app.route('/ready')
def ready():
    return jsonify(status="ready"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

