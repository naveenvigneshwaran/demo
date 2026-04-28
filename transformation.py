import cv2 as cv
import numpy as np
img = cv.imread('vending QR1.png')
cv.imshow('vending QR1', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
translated = translate(img, 100, 100)       

translated = translate(img, -200, 100)
cv.imshow('Translated', translated)
cv.waitKey(0)
# rotation 

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

#flipping
flipped = cv.flip(img, 0)
cv.imshow('Flipped', flipped)   
cv.waitKey(0)

ret, thresh = cv.threshold(blank, 150, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded', thresh)    
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')   
cv.drawContours(blank, contours, -1, (0, 0, 225), 1)
cv.imshow('Contours drawn', blank)      
cv.waitKey(0)
