import cv2 as cv
img = cv.imread('vending QR1.png')
cv.imshow('vending QR1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('vending QR1 gray', gray)     

#simple thresholding
ret, thresh1 = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('vending QR1 simple thresh', thresh1)
cv.waitKey(0)