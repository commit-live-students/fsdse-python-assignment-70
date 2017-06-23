import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
array2 = [10, 30, 40]

def solution(array1, array2):
    """
    Enter your code here
    """
    l = []
    new_array2 = np.array(array2)
    for i in array1:
        if i in np.nditer(new_array2):
            l.append(i)
        else:
            pass
    arr3 = np.array(l)
    return arr3
