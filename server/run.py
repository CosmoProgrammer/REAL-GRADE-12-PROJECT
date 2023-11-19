from flask import Flask, request, jsonify
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

@app.route('/getrow/<id>', methods=['GET'])
def get_row(id):
   # Fetch data for the row with the given id
   # Laaksh can you little bit hurry up, thanks
   row_data = {"ID":1, "Public/NonPublic":"Public", "Qty":[[
        ["Public"],
        ["Private"],
      ],[5, 10]], "Industry":"Cooking", "Types":[[
        ["Taste"],
        ["Colour"],
        ["Smell"],
      ],["Sweet", "Green", "Pungent"]]}
   return jsonify(row_data)

@app.route('/postrow/<id>', methods=['POST'])
def post_row(id):
   # Update the row with the given id
   # Hurry up just a little, thank you
   updated_row_data = request.get_json()
   return jsonify(updated_row_data), 200

if __name__ == '__main__':
   app.run()