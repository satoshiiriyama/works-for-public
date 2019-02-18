from flask import Flask, jsonify, render_template, request, make_response

import boto3
import json

# AWS s3 ID & Secret Key created on 12/21/2018 
s3_id = ***Confidential
s3_secret = ***Confidential

# AWS s3 bucket name and file name 
bucket = ***Confidential
file_name = ***Confidential


app = Flask(__name__)


@app.route("/")
def index():
    if request.authorization and request.authorization.username == "visitmore" and request.authorization.password == "sellmore":
        return render_template("index.html")

    return make_response('Could not verify.', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})


@app.route("/***Confidential")
def getdata():
    if request.authorization and request.authorization.username == "visitmore" and request.authorization.password == "sellmore":
        s3client = boto3.resource('s3', aws_access_key_id=s3_id, aws_secret_access_key=s3_secret)
        content_object = s3client.Object(bucket, file_name)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        return jsonify(json_content)
    
    return make_response('Could not verify.', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
    

if __name__ == "__main__":
    app.run(debug=True)