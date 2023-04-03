# day1_2_rot90.py
import numpy as np
import matplotlib.pyplot as plt
theta = np.radians(-90) #시계방향
c, s = np.cos(theta), np.sin(theta)
r = np.array(((c, -s), (s, c)))
t = np.array((1,0))
v = np.array((0,1)) + t
plt.plot(v[0], v[1], "rs") # 사각형
plt.plot(r.dot(v)[0], r.dot(v)[1], 'bo') #파란색 동그라미
plt.show()