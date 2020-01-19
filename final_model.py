import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D, BatchNormalization, LeakyReLU
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.models import model_from_yaml

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "../img/train"
class_names = ['battery','camera_battery', 'cardboard','clothes','contaminated_plastic','glass', 'human', 'keyboard','metal','mouse','pak','pants','paper', 'pen','phone', 'plastic','wrapper']
class_num = len(class_names)
print(class_num)
total = 0

for name in class_names:
    name_path = os.path.join(path, name)
    num = len(os.listdir(name_path))
    total += num
    print("Number of " + name + " image:" + str(num))

print("Total number of image: " + str(total))

batch_size = 128
epochs = 35
IMG_HEIGHT = 150
IMG_WIDTH = 150

data_generator = ImageDataGenerator(rescale=1./255,
                                    rotation_range=45,
                                    width_shift_range=.15,
                                    height_shift_range=.15,
                                    horizontal_flip=True,
                                    zoom_range=0.5
                                   )

data_gen = data_generator.flow_from_directory(batch_size=batch_size,
                                              directory=path,
                                              shuffle=True,
                                              target_size=(IMG_HEIGHT, IMG_WIDTH),
                                              class_mode='sparse')

model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.2),
    Dense(class_num, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit_generator(
    data_gen,
    steps_per_epoch=total // batch_size,
    epochs=epochs
)

# serialize model to YAML
model_yaml = model.to_yaml()
with open("model_1.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)

# serialize weights to HDF5
model.save_weights("model_1.h5")