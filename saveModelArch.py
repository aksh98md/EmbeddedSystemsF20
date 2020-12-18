import os
import cv2
import numpy as np
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model, Sequential

pic_size = 128
classes = 8 


model = Sequential([
    Conv2D(64, 3, activation='relu', input_shape=(pic_size,pic_size,1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(32, 3, activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    
    Dense(classes, activation='softmax')
])

model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

import json
model_json = model.to_json()
with open("model_trained.json", "w") as json_file:
    json.dump(model_json, json_file)