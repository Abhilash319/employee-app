from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 101, "name": "John"},
    {"id": 102, "name": "David"},
    {"id": 103, "name": "Smith"}
]

@app.route('/')
def home():
    return "<h1>Employee Management System</h1>"

@app.route('/employees')
def get_employees():
    return jsonify(employees)

@app.route('/health')
def health():
    return {"status": "UP"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)