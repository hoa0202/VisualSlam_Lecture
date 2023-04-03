# day1_6_fast.py
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys
img = cv.imread("c:/VIsualSLAM/VisualSlam_Lecture/simple3.png", 0)
fast = cv.FastFeatureDetector_create()
kp = fast.detect(img,None)
img2 = cv.drawKeypoints(img, kp, None, color =(0, 0, 255))
print(f"Threshold: {fast.getThreshold()}")
print(f"NonMaxSuppression: {fast.getNonmaxSuppression()}")
print(f"neighborhood: {fast.getType()}")
print(f"# of keypoint with NMS: {len(kp)}")
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)
print(f"# of keypoint without NMS: {len(kp)}")


if img is None:
    print('Image load failed')
    sys.exit()
cv.imshow("test", img2)
cv.waitKey()