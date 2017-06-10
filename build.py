import numpy as np


def solution(array1, array2):
    array1 = np.array([0, 10, 20, 40, 60])

    array2 = [10, 30, 40]

    return (np.intersect1d(array1, array2))

print solution([ 0 ,10, 20, 40, 60] , [10, 30, 40])
