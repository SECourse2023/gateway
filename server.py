from flask import Flask, request, jsonify
from register import register_do

app = Flask(__name__)

# Define a route that listens to HTTP POST requests
@app.route('/register', methods=['POST'])
def handle_request():
    request_content = request.get_json()
    result = register_do(request_content)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8000)
