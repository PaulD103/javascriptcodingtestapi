from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data')
def get_data():
    return {'data': 'This is the data of your api!'}
