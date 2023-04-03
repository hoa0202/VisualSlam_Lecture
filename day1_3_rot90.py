# day1_3_rot90.py
import numpy as np
import matplotlib.pyplot as plt
theta = np.radians(-90) #시계방향
c, s = np.cos(theta), np.sin(theta)
r = np.array(((c, -s), (s, c)))
t = np.array((1,0))
v = np.array(((8,8), (10,6), (10,4), (6,4), (6,6), (8,8))) \
    - np.array((8,6)) #다음줄로 넘겨서 작성을 원할경우 \ 역슬레쉬 추가
plt.plot(v[:, 0], v[:, 1], "r") #앞에 행을 전부 가져가기위해 :을 사용
# plt.plot(v@r[:, 0], v@r[:, 1], 'b') #2행 2열이 6행 2열과 연산하기위해 v@r 사용
plt.plot(v@r[:, 0], v@r[:, 1], 'b') #회전이후의 도형

plt.show()