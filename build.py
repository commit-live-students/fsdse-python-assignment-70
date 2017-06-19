import numpy as np

def solution(array1, array2):
    boo=np.in1d(array1,array2)
    return np.array(array1)[boo]
