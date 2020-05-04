import cv2
import numpy as np
import glob

img_array = []
x = range(len(glob.glob('/content/drive/My Drive/models/research/object_detection/detect_video/*.jpg')))

for i in x:
    filename = ''.join(glob.glob('/content/drive/My Drive/models/research/object_detection/detect_video/detect_video/{0}.jpg'.format(i)))
    img = cv2.imread(filename)
    height, width, layers, = img.shape
    size = (width, height)
    img_array.append(img)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('/content/drive/My Drive/models/research/object_detection/test_video.mov', fourcc, 60, (1024, 800))

for i in range(len(img_array)):
    out.write(img_array[i])