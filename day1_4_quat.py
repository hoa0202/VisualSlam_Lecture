# day1_4_quat.py
import math, numpy as np

def euler_from_quaternion(x, y ,z, w):
    t0 = +2.0 * (w * x + y * y)
    t1 = +1.0 - 2.0 * (x * x + y * y) # x** + y** 같은 의미
    roll_x = math.atan2(t0, t1)
    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)
    return roll_x, pitch_y, yaw_z # in radians.
# print(euler_from_quaternion( 0, 0, 0.7072, 0.7072)) #결과 0.0, 0.0, 1.571..) #1.571 == 파이/2
print(euler_from_quaternion( 0, 0, np.sin(np.pi/4), np.sin(np.pi/4)))#오차를 줄이기위해 np.sin(np.pi/4)로 수정
from scipy.spatial.transform import Rotation as R
r= R.from_quat([0, 0, np.sin(np.pi/4), np.sin(np.pi/4)])
print(r.as_euler('xyz'))
r = R.from_euler('z', 90, degrees=True)
print(r.as_quat())
#www.andre-gaschler.com/rotationconverter