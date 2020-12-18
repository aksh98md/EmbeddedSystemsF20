#!/usr/bin/env python
# coding: utf-8


import cv2
import json
import random
import pygame
import sys, os
import operator
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json

# use pygame to build a perdiction frame
pygame.init()
screen = pygame.display.set_mode((400,400),pygame.RESIZABLE)
CLIP_X1,CLIP_Y1,CLIP_X2,CLIP_Y2 = 160,140,400,360

# read the trained model
with open('model_trained.json','r') as f:
    model_json = json.load(f)
loaded_model = model_from_json(model_json)
loaded_model.load_weights('model_trained.h5')

cap = cv2.VideoCapture(1) # open the camera
i = 0 # to record the image amount
wzs = 161 # adjust the binary threshold
image_q = cv2.THRESH_BINARY # adjust the mode of binary

while True:
    _, FrameImage = cap.read() # read the frame
    FrameImage = cv2.flip(FrameImage, 1) # flip the frame horizontally
    cv2.imshow("", FrameImage) # show the frame
    cv2.rectangle(FrameImage, (CLIP_X1, CLIP_Y1), (CLIP_X2, CLIP_Y2), (0,255,0) ,1) # mark the position of ROI

    ROI = FrameImage[CLIP_Y1:CLIP_Y2, CLIP_X1:CLIP_X2] # ROI的大小
    ROI = cv2.resize(ROI, (128, 128))  # ROI resize
    ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY) # turn ROI to grayscale
    _, output = cv2.threshold(ROI, wzs, 255, image_q) # Threshold Binary
    
    SHOWROI = cv2.resize(ROI, (256, 256)) # ROI resize
    _, output2 = cv2.threshold(SHOWROI, wzs, 255, image_q) # Black Background is better for prediction
    cv2.imshow("ROI", output2)

    # these lines are for training the data
    # cv2.imwrite('./test/handdata'+str(i)+'.jpg',output2)
    # i += 1
    # cv2.waitKey(100)

    
    result = loaded_model.predict(output.reshape(1,128, 128, 1)) 
    predict =   { '1':    result[0][0],
                  '2':    result[0][1],    
                  '3':    result[0][2],
                  '4':    result[0][3],
                  '5':    result[0][4],
                  'fist':    result[0][5],
                  'ok':    result[0][6],
                  'yo':    result[0][7],
                  }
    print(predict)
    predict = sorted(predict.items(), key=operator.itemgetter(1), reverse=True) # the one who get higher score will sort to the first place

    # show the result the trained model think is the answer, if no will show a nosign picture
    if(predict[0][1] == 1.0):
        predict_img  = pygame.image.load(os.getcwd() + '/Hand_gesture/dataset/' + predict[0][0] + '.png')
    else:
        predict_img  = pygame.image.load(os.getcwd() + '/Hand_gesture/dataset/no.png')
    predict_img = pygame.transform.scale(predict_img, (400, 400))
    screen.blit(predict_img, (0,0))
    pygame.display.flip()

    # additional function to do on the ROI with keyboard buttons
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('l'): # lower wzs quality
      wzs = wzs - 5
    elif interrupt & 0xFF == ord('u'): # upper wzs quality
      wzs = wzs + 5
    elif interrupt & 0xFF == ord ('s'): # save dataset
      cv2.imwrite('handdata'+str(random.randint(1,9999))+'.jpg',output2)
    elif interrupt & 0xFF == ord ('c'): # change THRESH_BINARY TO THRESH_BINARY_INV
      if image_q == cv2.THRESH_BINARY_INV:
        image_q = cv2.THRESH_BINARY
      else:
        image_q = cv2.THRESH_BINARY_INV
    if interrupt & 0xFF == ord('p'): # esc key
        break
            
pygame.quit()
cap.release()
cv2.destroyAllWindows()
