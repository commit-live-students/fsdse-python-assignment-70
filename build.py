import numpy as np

def solution(array1, array2):
    lis = []
    for i in array1:
        for j in array2:
            if (i == j):
                lis.append(i)
    return lis
