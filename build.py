import numpy as np

def solution(array1, array2):

    a1 = set(np.array(array1))
    a2 = set(np.array(array2))
    a = a1.intersection(a2)

    return sorted(list(a))

# solution([0,10, 20, 40, 60],[10, 30, 40])
# Output : [10, 40]
