from math import log


def log_array(arr):
    new_arr = [0] * len(arr)
    for i, val in enumerate(arr):
        new_arr[i] = log(val)
    return new_arr


def quadratic_array(arr):
    new_arr = [0] * len(arr)
    for i, val in enumerate(arr):
        new_arr[i] = val * val
    return new_arr


nArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
logArr = log_array(nArray)
quadraticArr = quadratic_array(nArray)
print(logArr)
print(quadraticArr)
