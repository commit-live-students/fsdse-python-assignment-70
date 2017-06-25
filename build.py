import numpy as np

def solution(array1, array2):
    np_array1 = np.array(array1)
    np_array2 = np.array(array2)
    np_array3 = []
    for item in np_array2:
        if item in np_array1:
            np_array3.append(item)
    return np_array3
