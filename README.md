# Lung Disease Classification Using MobileNetV3 Architecture

## GitAds Sponsored

[![Sponsored by GitAds](https://gitads.dev/v1/ad-serve?source=nineone-code/classification-lung-disease-api@github)](https://gitads.dev/v1/ad-track?source=nineone-code/classification-lung-disease-api@github)

📱 **Try our mobile app!** Download it now from the Google Play Store: [LungLens - Lung Disease Classification](https://play.google.com/store/apps/details?id=com.nineone.lunglens)

This is my final college project, I have developed a convolutional neural network (CNN) for the classification of lung diseases. The CNN is based on the MobileNetV3 architecture, which has been modified and fine-tuned for this particular task.

The CNN is able to classify lung diseases into four different classes: normal, tuberculosis, pneumonia, and COVID-19. To train the model, I have used a large dataset of Xray images of the lungs, which was obtained from the Kaggle platform. The training process was performed on [Google Colab](https://colab.research.google.com/drive/1LWosgRLUPnHR-HXjygYE_gq1Gl7sQusd?usp=sharing), a cloud-based platform for machine learning and data science, which provided access to powerful GPUs and TPUs for fast training and inference.

```bash
python3 -m venv myenv
```

then:

```bash
. myenv/bin/activate
```

Once the model was trained, I implemented it as a web application using Flask, a lightweight Python web framework. Flask made it easy to build and deploy the application, and offered a range of tools and resources for creating dynamic and interactive web applications. To implement my project, I first installed Flask and any other dependencies that my application required. I used a requirements.txt file to specify the packages and versions that my application needed, and used [pip](https://pip.pypa.io/en/stable/), the Python package manager, to install these packages automatically.

to install library:

```bash
pip install -r requirements.txt
```

OR

```bash
pip install -t lib -r requirements.txt
```

For the frontend of the application, I used Flutter, a mobile app development framework. Flutter allowed me to create a user-friendly interface for interacting with the model, and made it easy to build a cross-platform application that could be used on both Android and iOS devices.

Overall, the combination of MobileNetV3, Kaggle, Google Colab, Flask, and Flutter was key to the success of my project, and allowed me to develop a high-performing and user-friendly application for the classification of lung diseases.

For deployment you can write code like this:

```bash
gunicorn app:app
```

OR

```bash
gunicorn app:app -b localhost:5000
```

```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
