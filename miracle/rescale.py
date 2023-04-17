# -*- coding: utf-8 -*-
"""
Created on Fri May 27 00:33:20 2022

@author: User
"""


import cv2 as cv

# Image scaling and resizing
img = cv.imread('Images/wall.jpg')
# cv.imshow('Cat',img)

def rescale(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
# resized_image = rescale(img)
# cv.imshow('Image', resized_image)
capture = cv.VideoCapture('Videos/Microbots.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)   
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()