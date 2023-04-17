# -*- coding: utf-8 -*-
"""
Created on Mon May 30 21:04:18 2022

@author: User
"""

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[200:300,300:400] = 255,66,180
# cv.imshow('Color', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) # or cv=-1
# cv.imshow('Rectangle', blank)

# 3. Drawing a circle
# cv.circle(blank, (250,250), 40, (11,22,180), thickness=-1)
# cv.imshow('Circle', blank)

# 4. Drawing a line
# cv.line(blank, (100,300), (50,50), (0,0,190), thickness=10)
# cv.imshow('Line', blank)

# 5. Writing text in images
cv.putText(blank, 'Hello world', (50,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)


# img = cv.imread('Images/wall.jpg')
# cv.imshow('Assassin\'s Creed', img)

cv.waitKey(0)
