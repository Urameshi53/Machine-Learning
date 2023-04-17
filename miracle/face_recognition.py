# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 02:07:19 2022

@author: User
"""

import cv2 as cv

def rescale(frame, scale=0.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    
    return cv.resize(frame, dimension, cv.INTER_AREA)

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
people = ['Bill', 'Elon', 'Federal', 'Jeff', 'Mark']

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# img = cv.imread(r'C:\Users\User\Documents\Python\miracle\people\Federal\IMG-20220305-WA0008.jpg')
img = cv.imread(r"C:\Users\User\Documents\Python\miracle\people\Mark\1654557328891.jpg")
# img = cv.imread(r"C:\Users\User\Documents\Python\miracle\people\Jeff\1654565843606.jpg")
img = rescale(img,0.5)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1,4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    
cv.imshow('Detected Face', img)
cv.waitKey(0)
    