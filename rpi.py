import cv2
import json
import random
import sys, os
import operator
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json
import serial, json
from playKeystroke import *

maintain = 5
patience = 1000

option1 = "ttyACM0"
option2 = "ttyACM1"

port = option2

# run ls /dev/tty* before and after plugging in arduino to find out
ser = None
while ser is None:
    try:
        ser = serial.Serial('/dev/' + port, 9600)
    except:
        port = option1 if port == option2 else option2
        print(port)
    print(ser)

print("Setting up keyboard")
kb = Keyboard()
with open('gestureKeystrokeMapping.json') as json_file:
    gesturesKeystrokes = json.load(json_file)
for key,val in gesturesKeystrokes.items():
    if val:
        gesturesKeystrokes[key] = kb.loadFromPickle(val)
     #{"f": kb.loadFromPickle("commandShiftV"), "1": kb.loadFromPickle("commandShiftA")}

CLIP_X1,CLIP_Y1,CLIP_X2,CLIP_Y2 = 160,140,400,360

# Read model
with open('model_trained.json','r') as f:
    model_json = json.load(f)
# print(model_json)
loaded_model = model_from_json(model_json)
loaded_model.load_weights('model_trained.h5')

cap = cv2.VideoCapture(0) 
wzs = 88 # polarization
image_q = cv2.THRESH_BINARY_INV # image quality

arduinoOutput = ""

def runRecognition():
    global arduinoOutput, wzs, image_q
    finalPrediction = None
    predictions = []
    while finalPrediction is None or len(finalPrediction) > patience:
        _, FrameImage = cap.read() 
        FrameImage = cv2.flip(FrameImage, 1) # 圖像水平翻轉
        cv2.rectangle(FrameImage, (CLIP_X1, CLIP_Y1), (CLIP_X2, CLIP_Y2), (0,255,0) ,1) # 框出ROI位置

        ROI = FrameImage
        ROI = cv2.resize(ROI, (128, 128))  # ROI resize
        ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
        _, output = cv2.threshold(ROI, wzs, 255, image_q) # Threshold Binary
        
        cv2.imshow("", output)

        cv2.waitKey(10)
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
        predict = sorted(predict.items(), key=operator.itemgetter(1), reverse=True) 
        predictions.append(predict[0][0])

        if len(predictions) > maintain and len(set(predictions[-maintain:])) == 1: # if the last "maintain" number of predictions are the same
            finalPrediction = predictions[-1][0]

        interrupt = cv2.waitKey(10)
        if interrupt & 0xFF == ord('l'): # lower wzs quality
          wzs = wzs - 5
        elif interrupt & 0xFF == ord('u'): # upper wzs quality
          wzs = wzs + 5
        elif interrupt & 0xFF == ord ('c'): # change THRESH_BINARY TO THRESH_BINARY_INV
          if image_q == cv2.THRESH_BINARY_INV:
            image_q = cv2.THRESH_BINARY
          else:
            image_q = cv2.THRESH_BINARY_INV

    print("final prediction", finalPrediction)
    if gesturesKeystrokes[finalPrediction]:
        print("typing ", finalPrediction)
        kb.event_loop(gesturesKeystrokes[finalPrediction])

    arduinoOutput = ""

print("starting...")
while True:
    if not arduinoOutput:
        try:
            ser.flushInput()
        except:
            print("flush fail", sys.exc_info()[0])
            try:
                port = option1 if port == option2 else option2
                ser = serial.Serial('/dev/' + port, 9600)
            except:
                port = option1 if port == option2 else option2
                continue


        arduinoOutput = ser.readline()

    if arduinoOutput:
        print(arduinoOutput)
        runRecognition()

    