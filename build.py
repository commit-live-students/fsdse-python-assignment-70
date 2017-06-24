import numpy as np


def solution(array1, array2):
    """
    Enter your code here
    """
    common=[]
    for i in array1:
        for j in array2:
            if i==j:
                common.append(i)
    return np.array(common)
