# day2_1_orb.py
from skimage import data, transform as tf
from skimage.feature import ORB, match_descriptors, corner_harris, corner_peaks, plot_matches
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np, cv2

img1 = rgb2gray(data.astronaut())
img2 = tf.rotate(img1, 180)
tform = tf.AffineTransform(scale=(1.3, 1.0), rotation=0.5, translation=(0, -200))
img3 = tf.warp(img1, tform)

descriptor_extractor = ORB(n_keypoints=200)
descriptor_extractor.detect_and_extract(img1)
keypoints1 = descriptor_extractor.keypoints
descriptors1 = descriptor_extractor.descriptors

descriptor_extractor.detect_and_extract(img2)
keypoints2 = descriptor_extractor.keypoints
descriptors2 = descriptor_extractor.descriptors

descriptor_extractor.detect_and_extract(img3)
keypoints3 = descriptor_extractor.keypoints
descriptors3 = descriptor_extractor.descriptors

matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)
matches13 = match_descriptors(descriptors1, descriptors2, cross_check=True)
fig, ax = plt.subplots(nrows=2, ncols=1)
plt.gray()

plot_matches(ax[0], img1, img2, keypoints1, keypoints2, matches12)
plot_matches(ax[1], img1, img3, keypoints1, keypoints3, matches13)


plt.show()