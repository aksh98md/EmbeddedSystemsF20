#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from keras.utils import np_utils
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model, Sequential


# set the picture size and the data path
pic_size = 128
image_path = './Hand_gesture/dataset/trained_image/'

# print the total number of the image of each type in the dataset
for image_count in os.listdir(image_path):
    print(str(len(os.listdir(image_path + image_count))) + " " + image_count + " images")

# record the total number of the dataset image
file_count = 0
for floderName in os.listdir(image_path):
    for filename in os.listdir(image_path + floderName):
        file_count +=1
print('all_image_file: ',file_count)

# build a empty np_array for the label
label_default = np.zeros(shape=[file_count])
img_default = np.zeros(shape=[file_count,pic_size,pic_size])
file_count = 0

# mark the image with a label in each folder
for floderName in os.listdir(image_path):
    for filename in os.listdir(image_path + floderName):        
        print(image_path)
        print(floderName)
        temp = cv2.imread(image_path + floderName + "/" + filename,0)
        print(temp)
        print(image_path + floderName + "/" + filename)
        print(temp.shape)
        temp = cv2.resize(temp, (pic_size,pic_size))
        img_default[file_count] = temp
        
        if floderName == '1':
            label_default[file_count] = 0
        elif floderName == '2':
            label_default[file_count] = 1
        elif floderName == '3':
            label_default[file_count] = 2
        elif floderName == '4':
            label_default[file_count] = 3
        elif floderName == '5':
            label_default[file_count] = 4
        elif floderName == 'fist':
            label_default[file_count] = 5    
        elif floderName == 'ok':
            label_default[file_count] = 6
        elif floderName == 'yo':
            label_default[file_count] = 7
        file_count +=1

# reshape tp the dimension that is going to throw into the input
img_default = img_default.reshape(file_count,pic_size,pic_size,1)
img_default.shape

label_onehot=np_utils.to_categorical(label_default) # do onehot encoding
print('label_onehot[0]:{},label_dim:{},shape:{}'.format(label_onehot[0],label_onehot.ndim,label_onehot.shape)) # Label(Encoding result , dimension, shape)
img_default = img_default / 255.0 # do normalization


random_seed  = 3 # random segmentation
x_train, x_test, y_train, y_test = train_test_split(img_default, label_onehot, test_size = 0.2, random_state=random_seed) 
print('x_train.shape:{}\n,y_train.shape:{}\nx_test.shape:{}\ny_test.shape:{}'.format(x_train.shape, y_train.shape, x_test.shape, y_test.shape)) #(train_img, train_label, test_img, test_label)


#classes = 5 # 5 types of gestures
classes = 8 # 8 types of gestures

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
model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=20)

# store the trained model into json and h5 file
import json
model_json = model.to_json()
with open("model_trained.json", "w") as json_file:
    json.dump(model_json, json_file)
model.save("model_trained.h5")
