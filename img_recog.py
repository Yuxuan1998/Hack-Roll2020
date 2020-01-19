# import library
import sys
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import model_from_yaml

def img_recog(path):
    # label
    class_names = ['battery','camera_battery', 'cardboard','clothes','contaminated_plastic','glass', 'human', 'keyboard','metal','mouse','pak','pants','paper', 'pen','phone', 'plastic','wrapper']

    # load YAML and create model
    yaml_file = open('model_100.yaml', 'r')
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    loaded_model = model_from_yaml(loaded_model_yaml)

    # load weights into new model
    loaded_model.load_weights("model_100.h5")

    # compile model
    loaded_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # process image
    IMG_HEIGHT = 150
    IMG_WIDTH = 150

    img = image.load_img(path, target_size=(IMG_HEIGHT, IMG_WIDTH))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)/255

    # predict
    prediction = loaded_model.predict_classes(x)[0]
    prediction = class_names[prediction]

    return prediction

sys.modules[__name__] = img_recog

