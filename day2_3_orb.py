# day2_3_orb.py
from skimage import data, exposure
from skimage.feature import hog
import matplotlib.pyplot as plt

img = data.astronaut()
fd, hog_image = hog(img, orientations=8, ixel_per_cell=(16,16), cells_per_block=(1,1), visualize=True, multichannel=True)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex = True, sharey=True)
ax1. axis('off')
ax1. imshow(img, cmap=plt.cm.gray)
ax1.set_title('Input image')

hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()