import cv2 as cv
import numpy as np  
blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle',circle)
cv.waitKey(0)
# bitwise AND
bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwiseAnd)
#bitwise OR
bitwiseOr = cv.bitwise_or(rectangle, circle)        
cv.imshow('Bitwise OR', bitwiseOr)
#bitwise XOR
bitwiseXor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwiseXor)    
#bitwise NOT
bitwiseNot = cv.bitwise_not(circle) 
cv.imshow('Bitwise NOT', bitwiseNot)
cv.waitKey(0)