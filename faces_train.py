import os
import cv2 as cv
import numpy as np  
files = listdir("new folder")

people = ['smile.png']
DIR = r'C:\Users\navee\Desktop\opencv project\New folder'
haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')