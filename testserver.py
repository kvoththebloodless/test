from flask import Flask

from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import json
import uuid

app = Flask(__name__)



@app.route('/login',methods=['POST'])
def login():
    data = request.data
    dataDict = json.loads(data)
    if dataDict is not None and bool(dataDict):
        print(dataDict)
        return json.dumps('{token:'+str(uuid.uuid4())+'}'),200
    else:
        return "this password is incorrect",400

@app.route('/register',methods=['POST'])
def register():
    data = request.data
    dataDict = json.loads(data)
    if dataDict is not None and bool(dataDict):
        print(dataDict)
        return json.dumps('{token:'+str(uuid.uuid4())+'}'),200
    else:
        return "this username is already taken",400


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)