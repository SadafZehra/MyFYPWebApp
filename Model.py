#!/usr/bin/env python
# coding: utf-8

# In[4]:
config = {
    "apiKey": "AIzaSyDh2fn6QMGcDBaP7_DlwrDUngg9Xr1V0mw",
    "authDomain": "bankingappbyaj.firebaseapp.com",
    "databaseURL": "https://bankingappbyaj-default-rtdb.firebaseio.com",
    "projectId": "bankingappbyaj",
    "storageBucket": "bankingappbyaj.appspot.com",
    "messagingSenderId": "609572537357",
    "appId": "1:609572537357:web:655ed1404976ed3fc68144",
    "measurementId": "G-E8H7F5QQYX"
  }





import numpy as np
import cv2
#import matplotlib.pyplot as plt


import pyrebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()
   
# In[34]:


def XrayAnalyzer(path):
    image = cv2.imread(path)
    image = cv2.resize(image, (500,500))
    mask = np.zeros(image.shape, dtype='uint8')
    array = np.array([(201, 59), (174, 66), (148, 97), (112, 128), (87, 179), (72, 224), (67, 278), (64, 320), (58, 368), (56, 408), (56, 445), (57, 489), (67, 498), (88, 497), (111, 494), (135, 496), (158, 497), (186, 497), (213, 495), (241, 496), (258, 496), (283, 498), (301, 496), (321, 497), (345, 496), (366, 496), (391, 495), (413, 495), (438, 497), (437, 481), (440, 459), (440, 432), (439, 410), (439, 386), (434, 355), (432, 333), (432, 305), (431, 284), (428, 264), (423, 237), (423, 214), (412, 189), (408, 171), (403, 157), (395, 144), (385, 127), (364, 113), (348, 95), (328, 83), (308, 74), (286, 71), (273, 82), (252, 90), (228, 90), (219, 71)])
    #Its use for segmentation
    mask = cv2.fillPoly(mask,[array], (255, 255, 255))
    #Morpholigical
    kernel = np.ones((3,3),np.uint8)
    dilation = cv2.dilate(mask,kernel,iterations = 3)
    
    result = cv2.bitwise_and(image, dilation)
    pathnew = path[22:] 
    print(pathnew,"path")
    cv2.imwrite("H:/DatabaseData/Result/"+pathnew, result)
    img = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
    count50 = 0
    count100 = 0
    count150 = 0
    count200 = 0
    count250 = 0
    for i in range(len(img)):
        for j in range(len(img)):
            
            if img[i][j] >= 0 and img[i][j] <= 50:
                #print(img[i][j])
                count50 +=1
            elif img[i][j] >= 50 and img[i][j] <= 100:
                #print(img[i][j])
                count100 +=1
            elif img[i][j] >= 100 and img[i][j] <= 150:
                #print(img[i][j])
                count150 +=1
            elif img[i][j] >= 150 and img[i][j] <= 200:
                #print(img[i][j])
                count200 +=1
            elif img[i][j] >= 200 and img[i][j] <= 250:
                #print(img[i][j])
                count250 +=1
    Totalcount = count50 + count100
    #if count50 >= count100 and count50 >= count150 and count50 >= count200 and count50 >= count250:
    if Totalcount >= count150 and Totalcount >= count200 and Totalcount >= count250:
        a="Low Severe"
    else:
        a = "High Severe"
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    hist = hist.flatten()
    hist = hist.tolist()
    result = result.tolist()
    
    storage.child("images_frommodel/"+pathnew).put("H:/DatabaseData/Result/"+pathnew)
    db.child("images_frommodel").push({
        "image":pathnew,
        "read":True
    })
    return a,hist

# XrayAnalyzer("H:/DatabaseData/Input/1.jpg")

