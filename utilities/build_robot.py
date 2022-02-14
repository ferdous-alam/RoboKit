import numpy as np


class Robot:
    def __init__(self):
        self.frames = []
        self.child = None

    def make_frame(self, Rot_mat, pos_vec, w_vec, v_vec, p_c=None, mass=None):
        M_mat = np.array([[Rot_mat[0, 0], Rot_mat[0, 1], Rot_mat[0, 2], pos_vec[0]],
                          [Rot_mat[1, 0], Rot_mat[1, 1], Rot_mat[1, 2], pos_vec[1]],
                          [Rot_mat[2, 0], Rot_mat[2, 1], Rot_mat[2, 2], pos_vec[2]],
                          [0, 0, 0, 1]])
        Mc = np.array([[1, 0, 0, p_c[0]], [1, 0, 0, p_c[1]],
                       [1, 0, 0, p_c[2]], [0, 0, 0, 1]]) if p_c else None

        frame = {'mass': mass,
                 'M': M_mat,
                 'Mc': Mc,
                 'omega': np.array(w_vec).reshape(-1, 1),
                 'velocity': np.array(v_vec).reshape(-1, 1)}
        self.frames.append(frame)


if __name__ == "__main__":
    R, p, w, v, pc = np.eye(3), [0, 0, 1.0], [1, 2, 3], [4, 5, 6], [1, 2, 3]
    robot = Robot()
    robot.make_frame(R, p, w, v, pc)
    robot.make_frame(R, p, w, v, pc)
    robot.make_frame(R, p, w, v, pc)
    robot.make_frame(R, p, w, v, pc)
    robot.make_frame(R, p, w, v, pc)





