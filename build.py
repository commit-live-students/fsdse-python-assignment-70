import numpy as np


def solution(array1, array2):
    set_a = set(array1)
    set_b = set(array2)
    list_o = sorted(list(set_a & set_b))
    return list_o
