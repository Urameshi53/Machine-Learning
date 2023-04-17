# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:36:08 2022

@author: Lancelot
"""


import cv2 as cv
import numpy as np

def rescale(frame, scale=0.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    
    return cv.resize(frame, dimension, cv.INTER_AREA)

img = cv.imread('Images/people.jpg')
img = rescale(img)
cv.imshow('Test', img)

def brighten(image,beta = 70):
    new_image = np.zeros(img.shape, img.dtype)
    new_image = cv.convertScaleAbs(img, beta=beta)
    return new_image

cv.imshow('New Image', brighten(img))

cv.waitKey(0)

