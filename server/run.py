from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def helloWorld():
    return 'Hello, world'

@app.route('/config', methods=['POST'])
def handle_config():
    data = request.get_json()
    print(data)
    return {"message": "Config received"}, 200

if __name__ == '__main__':
   app.run()