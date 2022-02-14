import numpy as np
from utilities.build_robot import Robot

# robot specs
robot = Robot()
l_0 = 1.0
l_1 = 2.0
l_2 = 2.0

# frame 1
R, p, w, v = np.eye(3), [0, 0, l_0], [0, 0, 1], [0, 0, 0]
robot.make_frame(R, p, w, v)
# frame 2
R, p, w, v = np.eye(3), [0, l_1, l_0], [0, 0, 1], [l_1, 0, 0]
robot.make_frame(R, p, w, v)
# frame 3
R, p, w, v = np.eye(3), [0, l_1 + l_2, l_0], [0, 0, 1], [l_1 + l_2, 0, 0]
robot.make_frame(R, p, w, v)
# frame 4
R, p, w, v = np.eye(3), [0, l_1 + l_2, l_0], [0, 0, 0], [0, 0, 1]
robot.make_frame(R, p, w, v)


