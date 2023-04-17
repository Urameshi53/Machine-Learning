# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:06:59 2022

@author: User
"""


import cv2 as cv

def rescale(frame, scale=0.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    
    return cv.resize(frame, dimension, cv.INTER_AREA)

img = cv.imread('Images/people.jpg')
img = rescale(img)
# cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 20)

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected face', img)
cv.waitKey(0)
