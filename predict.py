import cv2
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.optimizers import Adam
from keras.utils import img_to_array
from PIL import Image

file_model = "model/model_mobileNetV3-91.h5"
file_model_2 = "model/xray_nonxray.h5"
labels = ["Covid-19", "Normal", "Tuberkolosis", "Pneumonia"]
labels_2 = ["nonxray", "xray"]


def predict(path):
    model_2 = load_model(file_model_2, compile=False)
    model = load_model(file_model, compile=False)
    data = np.zeros((1, 224, 224, 3))
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    pil_img = Image.fromarray(img)
    data[0] += img_to_array(pil_img)
    y_pred = model_2.predict(data)

    dict_result_1 = {}
    for i in range(2):
        dict_result_1[y_pred[0][i]] = labels_2[i]
    penentuan = y_pred[0]
    penentuan.sort()
    penentuan = penentuan[::-1]
    prob = penentuan[:4]
    prob_result = []
    class_result = []
    for i in range(2):
        prob_result.append((prob[i] * 100).round(2))
        class_result.append(dict_result_1[prob[i]])
    if class_result[0] == "nonxray" or y_pred[0][0] >= 0.1:
        class_result = labels_2
        return class_result, prob_result, y_pred

    y_pred = model.predict(data)
    dict_result = {}
    for i in range(4):
        dict_result[y_pred[0][i]] = labels[i]
    res = y_pred[0]
    res.sort()
    res = res[::-1]
    prob = res[:4]
    prob_result = []
    class_result = []
    for i in range(4):
        prob_result.append((prob[i] * 100).round(2))
        class_result.append(dict_result[prob[i]])

    return class_result, prob_result, y_pred
