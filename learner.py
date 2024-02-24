## THIS FILE IS DESIGNED TO PERMIT SOME FACE RECOGNITION 
## IT WILL USE THE SYSTEM PICTURE INPUT 

##DEPENDENCIES TO INTERACT WITH THE SYSTEM
import os
import cv2
import numpy as np
import face_recognition
from PIL import Image
from datetime import datetime
import time
import sys

path = './images/'

mesImages = []

myList = os.listdir(path)

print(myList)

## ANALYSIS OF THE PICTURES IN DATABASE
