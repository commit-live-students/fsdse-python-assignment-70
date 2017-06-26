import numpy as np

def solution(array1, array2):
    a = np.array(array1)
    b = np.array(array2)
    c = np.intersect1d(array1,array2)
    return c
