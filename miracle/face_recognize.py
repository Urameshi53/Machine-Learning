# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:03:26 2022

@author: User
"""

import os
import cv2 as cv
import numpy as np

people = ['Bill', 'Elon', 'Federal', 'Mark', 'Jeff']
DIR = r'C:\Users\User\Documents\Python\miracle\people'

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, 1.1,4)
            
            for (x,y, w, h) in faces_rect:
                faces = gray[y:y+h, x:x+w]
                features.append(faces)
                labels.append(label)
                
create_train()
print('Training done ------')

features = np.array(features, dtype='object')
labels = np.array(labels)

# print('Length of the features is', len(features))
# print('Length of the labels', len(labels))   

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)
np.save('features.npy', features)
np.save('labels.npy', labels)