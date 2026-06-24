from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Employee Management System</h1>
    <h2>Welcome to CI/CD Demo Project</h2>
    """
    
@app.route('/health')
def health():
    return {"status": "UP"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)