import cv2 as cv
import numpy as np  

img = cv.imread('vending QR1.png')
cv.imshow('vending QR1', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
#Gaussion Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)
cv.waitKey(0)   
#bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 10)
cv.imshow('Bilateral Blur', bilateral)  
cv.waitKey(0)