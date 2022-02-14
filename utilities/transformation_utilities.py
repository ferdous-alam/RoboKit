import numpy as np


def get_rot_mat(T):
    """
    Takes a homogeneous transformation matrix
    and returns the corresponding rotation matrix
    and position vector

    :param T: 4 x 4 transformation matrix
    :return:
        rot_mat: 3 x 3 rotation matrix
        pos_vec: 3 x 1 position vector
    """
    rot_mat = T[0:3, 0:3]
    pos = T[0:3, -1]
    pos_vec = pos.reshape(-1, 1)  # convert to a column vector

    return rot_mat, pos_vec


def inv_transform(T):
    """
    takes a homogeneous transformation matrix and
    returns the corresponding inverse transformation matrix
    using the formula:

    inv_T = [R^T  -R^T * p
              0      1]

    :param T: 4 x 4 transformation matrix
    :return: 4 x 4 inverse transformation matrix
    """

    rot, pos = get_rot_mat(T)
    inv_T = np.r_[np.c_[rot.T, - np.matmul(rot.T, pos)],
                  np.array([0, 0, 0, 1]).reshape(1, -1)]
    return inv_T


def skew_matrix(w):
    """
    This function calculates the skew symmetric matrix of a 3-dimensional vector
    :param w: 3 x 1 vector
    :return: skew_w: 3 x 3 skew symmetric matrix of a 3 x 1 vector
    """
    skew_w = np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])
    return skew_w


def matrix_exponential(omega, vel, theta):
    """
    This function calculates the homogenous transformation matrix from a
    given set of angular velocity and linear velocity vectors obtained
    from the screw axis using the formula:


    T = exp^([S_i]*theta) = [exp^([omega]*theta)  alpha
                             0                    1]

    where,
        [omega] = skew symmetric matrix of omega
        S_i = ith screw axis described by omega and velocity
        exp^([omega]*theta) = I + sin(theta) + (1 - cos(theta))[omega]^2
        alpha = (I * theta + (1 - cos(theta))*[omega] + (theta - sin(theta)) * [omega]^2) * velocity

    :param:
        omega: angular velocity of a frame obtained from screw axis
        vel: linear velocity of a frame obtained from screw axis
        theta = angle
    :return: T: 4 x 4 transformation matrix
    """
    skew_omega = skew_matrix(omega)
    elem1 = np.eye(3) + np.sin(theta) * skew_omega + \
        (1 - np.cos(theta)) * np.matmul(skew_omega, skew_omega)
    temp = (np.eye(3) + (1 - np.cos(theta)) * skew_matrix(omega) + (
            theta - np.sin(theta)) * np.matmul(skew_omega, skew_omega))
    elem2 = np.matmul(temp, vel)
    T = np.r_[(np.c_[elem1, elem2], np.array([0, 0, 0, 1]).reshape(1, -1))]
    return T


if __name__ == "__main__":
    omega = np.array([1.0, 0, 0])
    vel = np.array([0, 0, 1.0])
    theta = 45

    T = matrix_exponential(omega, vel, theta)
    print(T)





