import numpy as np
import matplotlib.pyplot as plt
theta = np.radians(90)

r = np.array(( (np.cos(theta), -np.sin(theta)),
               (np.sin(theta), np.cos(theta)) ))
print('rotation matrix:')
print(r)

v = np.array((0,1))
plt.plot(v[0], v[1], 's')
print('vector v: ')
print(v)
print('apply the rotation matrix r to v: r*v')
print( r.dot(v) )
plt.plot(v[0], v[1], 'r^')
plt.plot(r.dot(v)[0], r.dot(v)[1], 'bo')
plt.show()
