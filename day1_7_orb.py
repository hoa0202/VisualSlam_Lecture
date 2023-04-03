# day1_7_orb.py
import cv2, numpy as np
img, img2 = cv2.imread("c:/VIsualSLAM/VisualSlam_Lecture/apple.jpg"), cv2.imread("c:/VIsualSLAM/VisualSlam_Lecture/apple2.jpg")
cv2.imshow("1", img)
cv2.imshow("2", img2)
# cv2.waitKey()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(40000, scaleFactor=1.2, nlevels=8, edgeThreshold=31, firstLevel=0, WTA_K=2, scoreType=cv2.ORB_HARRIS_SCORE, patchSize=31, fastThreshold=20)
kp1, des1 = orb.detectAndCompute(gray, None)
kp2, des2 = orb.detectAndCompute(img2, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = sorted(bf.match(des1, des2), key=lambda x: x.distance)
for i in matches[:100]:
    idx = i.queryIdx;   x1, y1 = kp1[idx].pt
    cv2.circle(img, (int(x1), int(y1)), 3, (255, 0, 0), 3)

for i in matches[:1000]:
    idx = i.queryIdx;   x1, y1 = kp2[idx].pt
    cv2.circle(img2, (int(x1), int(y1)), 3, (255, 0, 0), 3)
    
cv2.imshow("result", img)
cv2.imshow("result2", img2)
cv2.waitKey()
