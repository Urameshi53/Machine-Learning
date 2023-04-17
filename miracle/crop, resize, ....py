# -*- coding: utf-8 -*-
"""
Created on Mon May 30 21:26:08 2022

@author: User
"""

import cv2 as cv

def rescale(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    
    return cv.resize(frame, dimension, cv.INTER_AREA)

img = cv.imread('Images/wall.jpg')
img = rescale(img)
# cv.imshow('Cat', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), 1)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), cv.INTER_CUBIC)
# cv.imshow('Resized',resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)