from os import path
from flask import Flask, render_template, json


app = Flask(__name__)


# Displays json data to client
@app.route('/data', methods=['GET'])
def data():
    return render_template('disp_json.jinja', data=load_data())


# Loads json data from mock file. Can be retrofitted later to query database
def load_data():
    filename = path.join(app.root_path, 'MOCK_DATA.json')
    fp = open(filename)
    json_data = json.loads(json.dumps(fp.read()))
    return json_data
