import cv2
import numpy as np
from keras.models import load_model
from keras.utils import img_to_array
from PIL import Image

file_model = 'model/model_mobileNetV3-91.h5'
labels = ["Covid-19", "Pneumonia","Normal", "Tuberkolosis"]

def predict(path):
    model = load_model(file_model)
    data = np.zeros((1, 224, 224, 3))
    img = cv2.imread(path)
    img = cv2.resize(img,(224,224))
    pil_img = Image.fromarray(img)
    data[0]+=img_to_array(pil_img)
    # data/=255.0
    y_pred = model.predict(data)  

    dict_result = {}

    for i in range(4) :
        dict_result[y_pred[0][i]] = labels[i]
            
    res = y_pred[0]
    res.sort()
    res = res[::-1]
    prob=res[:4]
    prob_result =[]
    class_result=[]

    for i in range(4):
        prob_result.append ((prob[i]*100).round(2))
        class_result.append(dict_result[prob[i]])

    return class_result, prob_result