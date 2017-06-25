import numpy as np
array1=[0,10,20,40,60]
array2=[10,30,40]

def solution(array1, array2):
    common=np.intersect1d(array1, array2)
    return common
solution(array1,array2)
