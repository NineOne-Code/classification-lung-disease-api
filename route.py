import os

import cv2
import numpy as np
from flask import Flask, flash, jsonify, redirect, render_template, request
from werkzeug.utils import secure_filename

from predict import predict

app = Flask(
    __name__,
    static_url_path="/assets",
    static_folder="./public/assets",
    template_folder="./public",
)
app.config["SECRET_KEY"] = "secretkey"
app.config["UPLOAD_FOLDER"] = "public/assets/temp"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return post()
    else:
        return render_template("index.html")
        # return 'Welcome to My Classification Lung Disease API!!!'


@app.route("/api/predict", methods=["POST"])
def apiPredict():
    return postPredict()


def post():
    # check if the post request has the file part
    if "file" not in request.files:
        flash("No file part in the request")
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        flash("No file selected for uploading")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(path)
        print("path: ", path)
        pred = predict(path)

        file = cv2.imread(path)
        file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(path, file)
        resp = {}

        if len(pred[0]) == 2:
            print("predict 1: ", str(pred[0][0]) + str(len(pred[0])))
            resp = {
                "image": "temp/" + filename,
                "output": pred[0][0],
            }
        else:
            print("predict 2: ", str(pred[0][0]) + str(len(pred[0])))
            probability = {pred[0][i]: pred[1][i] for i in range(0, len(pred[0]))}
            resp = {
                "image": "temp/" + filename,
                "output": pred[0][0],
                "probability": probability,
            }
        return render_template("index.html", data=resp)
    else:
        flash("Allowed file types are png, jpg, jpeg")
        return redirect(request.url)


def postPredict():
    # check if the post request has the file part
    if "file" not in request.files:
        resp = jsonify({"message": "No file part in the request"})
        resp.status_code = 400
        return resp
    file = request.files["file"]
    if file.filename == "":
        resp = jsonify({"message": "No file selected for uploading"})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(path)
        pred = predict(path)
        resp = jsonify({})
        resp.status_code = 201

        resp = {}

        if len(pred[0]) == 2:
            print("predict 1: ", str(pred[0][0]) + str(len(pred[0])))
            resp = {
                "image": "temp/" + filename,
                "output": pred[0][0],
            }
        else:
            print("predict 2: ", str(pred[0][0]) + str(len(pred[0])))
            probability = {pred[0][i]: pred[1][i] for i in range(0, len(pred[0]))}
            resp = {
                "image": "temp/" + filename,
                "output": pred[0][0],
                "probability": probability,
            }
        return resp
    else:
        resp = jsonify({"message": "Allowed file types are png, jpg, jpeg"})
        resp.status_code = 400
        return resp
