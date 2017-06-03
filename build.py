import numpy as np


def solution(array1, array2):
    """
    Enter your code here
    """
    newArray = np.intersect1d(array1, array2)

    return newArray


array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 40])

print(solution(array1,array2))
