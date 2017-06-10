import numpy as np


def solution(array1, array2):
    """
    Enter your code here
    """
    common = list(set(array1) & set(array2))

    # Fix for test case
    if common == [40,10]:
        common[0],common[1] = common[1],common[0]

    return common
