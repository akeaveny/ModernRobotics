import numpy as np
np.set_printoptions(precision=3)

import modern_robotics as mr

if __name__ == '__main__':

    ###################
    # UWRT ARM CONFIG
    ###################
    l0, l1, l2, l3, l4 = 0.05, 0.286, 0.462, 0.356, 0.228
    m1, m2, m3, m4, m5, m6 = 5, 1, 3, 3, 0.25, 0.01 # TODO: link masses

    ###################
    # init params
    ###################

    # TODO: Input theta's???
    thetalist = np.array([0.1, 0.1, 0, 0.1, 0.1, 0.1])

    # screw axis
    Slist = np.array([[0, 0, 1, 0, 0, 0],       # turntable
                      [1, 0, 0, 0, 0, 0],       # lin actutor
                      [1, 0, 0, 0, l1, 0],      ### TODO: FIXED SHOULDER JOINT
                      [1, 0, 0, 0, l1, l2],     # elbow
                      [1, 0, 0, 0, l1, l2+l3],  # wrist pitch
                      [0, 1, 0, l1, 0, 0]]).T   # wrist roll

    # transformation matrices
    M00 = np.array([[ 1, 0, 0, 0], # turntable height
                    [ 0, 1, 0, 0],
                    [ 0, 0, 1, l0],
                    [ 0, 0, 0, 1]])
    M01 = M12 = np.array(np.eye(4))
    M23 = np.array([[ 1, 0, 0, 0],
                    [ 0, 1, 0, 0],
                    [ 0, 0, 1, l1],
                    [ 0, 0, 0, 1]])
    M34 = np.array([[1, 0, 0, 0],
                    [0, 1, 0, l2],
                    [0, 0, 1, l1],
                    [0, 0, 0, 1]])
    M45 = np.array([[1, 0, 0, 0],
                    [0, 1, 0, l3],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    M56 = np.array(np.eye(4))
    Mlist = np.array([M00, M01, M12, M23, M34, M45, M56])

    # # TODO: updated inertias
    G1 = np.diag([0.0135416666667, 0.025, 0.0135416666667, m1, m1, m1])
    G2 = np.diag([0.00702466666667, 0.00764966666667, 0.00104166666667, m2, m2, m2])
    G3 = np.diag([0.053986, 0.055861, 0.003125, m3, m3, m3])
    G4 = np.diag([0.032309, 0.034184, 0.003125, m4, m4, m4])
    G5 = np.diag([5.41666666667e-05, 5.41666666667e-05, 0.000104166666667, m5, m5, m5])
    G6 = np.diag([0.00227016666667, 0.00227016666667, 0.000208333333333, m6, m6, m6])
    Glist = np.array([G1, G2, G3, G4, G5, G6])

    ###################
    # Mass Matrix
    ###################
    M = mr.MassMatrix(thetalist, Mlist, Glist, Slist)
    print("UWRT ARM Mass Matrix: \n", M)