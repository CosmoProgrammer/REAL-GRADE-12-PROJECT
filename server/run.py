from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlAPI.main as main

app = Flask(__name__)
CORS(app)


@app.route('/')
def helloWorld():
    return 'Hello, world'


@app.route('/login/<username>/<password>', methods=['GET'])
def login(username, password):
    print(username, password)
    # print(main.login(username, password))
    return jsonify(main.login(username, password))


@app.route('/getdatafalse', methods=['GET'])
def getDataFalse():
    print('hi')
    l = main.returnAll(False)
    print(l)
    return jsonify(l)


@app.route('/getdatatrue', methods=['GET'])
def getDataTrue():
    print('hi')
    l = main.returnAll(True)
    print(l)
    return jsonify(l)


@app.route('/config', methods=['POST'])
def handle_config():
   # {'schema': [{'name': 'ID', 'type': 'number', 'subColumns': []}, {'name': 'Public/NonPublic', 'type': 'string', 'subColumns': []}, {'name': 'Qty', 'type': 'number', 'subColumns': [{'name': 'Public', 'type': 'number'}, {'name': 'Private', 'type': 'number'}]}, {'name': 'Industry', 'type': 'string', 'subColumns': []}, {'name': 'ExpiryDate', 'type': 'date', 'subColumns': []}, {'name': 'Type', 'type': 'string', 'subColumns': [{'name': 'Taste', 'type': 'string'}, {'name': 'Smell', 'type': 'string'}, {'name': 'Colour', 'type': 'string'}]}], 'users': [{'username': 'Anirudh', 'password': 'test1234', 'accessLevel': 'Admin'}, {'username': 'UserMax', 'password': 'qwerty', 'accessLevel': 'Level 1'}, {'username': 'Laaksh', 'password': 'KrishHasAnAss', 'accessLevel': 'Level 3'}]}   '''
    data = request.get_json()
    print(data)
    main.createTable(data['schema'])
    main.createLoginTable(data['users'])

    return {"message": "Config received"}, 200


@app.route('/getrow/<id>', methods=['GET'])
def get_row(id):
   # Fetch data for the row with the given id
   # Laaksh can you little bit hurry up, thanks
    row_data = {"ID": 1, "Public/NonPublic": "Public", "Qty": [[
        ["Public"],
        ["Private"],
    ], [5, 10]], "Industry": "Cooking", "Types": [[
        ["Taste"],
        ["Colour"],
        ["Smell"],
    ], ["Sweet", "Green", "Pungent"]]}
    return jsonify(list(main.getRow(id).items()))


@app.route('/addrow/<id>', methods=['POST'])
def post_row(id):
    # Update the row with the given id
    # Hurry up just a little, thank you
    updated_row_data = request.get_json()
    main.addRow(updated_row_data)
    return jsonify(updated_row_data), 200


@app.route('/deleterow/<id>', methods=['POST'])
def delete_row(id):
    # Update the row with the given id
    # Hurry up just a little, thank you
    print("GU")
    main.deleteRow(id)
    return jsonify('hi'), 200


@app.route('/editrow/<id>', methods=['POST'])
def edit_row(id):
    # Update the row with the given id
    # Hurry up just a little, thank you
    updated_row_data = request.get_json()
    main.updateRow(updated_row_data)
    return jsonify(updated_row_data), 200


# Another login function, Ill send you credentials and you will have to validate
'''
{'data': [
        [1, "Public", [5, 10], "Cooking", ["Sweet", "Green", "Pungent"]],
        [2, "Public", [6, 20], "Baking", ["Sour", "Blue", "Pleasant"]],
        [3, "NonPublic", [5, 5], "Cooking", ["Spicy", "Green", "None"]],
    ], 'schema': [
        {'name': "ID", 'type': "number", subColumns: []},
        {'name': "Public/NonPublic", 'type': "string", subColumns: []},
        {
            'name': "Qty",
            'type': "number",
            'subColumns': [
                {'name': "Public", type: "number"},
                {'name': "Private", type: "number"},
            ],
        },
        {'name': "Industry", 'type': "string", 'subColumns': []},
        {
            'name': "Types",
            'type': "string",
            'subColumns': [
                {'name': "Taste", 'type': "string"},
                {'name': "Colour", 'type': "string"},
                {'name': "Smell", 'type': "string"},
            ],
        },
        {'name': "Edit", 'type': "button", subColumns: []},
        {'name': "Delete", 'type': "button", subColumns: []},
    ]}
'''

if __name__ == '__main__':
    app.run()
