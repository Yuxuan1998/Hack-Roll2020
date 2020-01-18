# import library
import sys
import tensorflow as tf
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import model_from_yaml

def img_recog(path):
    # label
    class_names = ['battery', 'cardboard','clothes','contaminated_plastic','glass', 'human', 'keyboard','metal','mouse','pak','pants','paper', 'pen','phone', 'plastic','wrapper']

    # load YAML and create model
    yaml_file = open('model.yaml', 'r')
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    loaded_model = model_from_yaml(loaded_model_yaml)

    # load weights into new model
    loaded_model.load_weights("model.h5")

    # compile model
    loaded_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # process image
    IMG_HEIGHT = 150
    IMG_WIDTH = 150

    predict_img = cv2.imread(path)
    predict_img = cv2.resize(predict_img,(IMG_HEIGHT,IMG_WIDTH))
    predict_img = np.reshape(predict_img,[1,IMG_HEIGHT,IMG_WIDTH,3])

    # predict
    prediction = loaded_model.predict(predict_img)
    prediction_indices = np.argmax(prediction, axis=1)
    prediction = class_names[prediction_indices[0]]

    return prediction

sys.modules[__name__] = img_recog

