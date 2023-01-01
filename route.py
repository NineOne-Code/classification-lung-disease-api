import os

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

from predict import predict

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'temp'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return postPredict()
    else:
        return 'Hi!'


def postPredict():
    # check if the post request has the file part
    if 'file' not in request.files:        
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        pred = predict(path)
        probability = {pred[0][i]: pred[1][i] for i in range(0, len(pred[0]))}
        print(probability)
        resp = jsonify({
            'message' : 'successfully', 
            'output': pred[0][0],
            'probability': probability,
            })
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message' : 'Allowed file types are png, jpg, jpeg'})
        resp.status_code = 400
        return resp