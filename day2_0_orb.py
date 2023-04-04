# day2_0_orb.py
from skimage.feature import ORB, match_descriptors
import numpy as np, cv2
img1 = np.zeros((100,100))
img2 = np.zeros_like(img1)
np.random.seed(1)
square = np.random.rand(20,20)
img1[40:60, 40:60] = square
img2[53:73, 53:73] = square
detector_extractor1 = ORB(n_keypoints=5)
detector_extractor2 = ORB(n_keypoints=5)
detector_extractor1.detect_and_extract(img1)
detector_extractor2.detect_and_extract(img2)
matches = match_descriptors(detector_extractor1.descriptors, detector_extractor2.descriptors)

print("matches\n",matches)
print("\ndetector_extractor1\n",detector_extractor1.keypoints[matches[:, 0]])
print("\ndetector_extractor2\n",detector_extractor2.keypoints[matches[:, 1]])

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey()