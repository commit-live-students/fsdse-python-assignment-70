import numpy as np


def solution(array1, array2):
    return np.intersect1d(np.array(array1), np.array(array2))
