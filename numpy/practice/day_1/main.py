import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

arr2d = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2d)
print(arr2d.ndim)
print(arr2d.shape)
print(arr2d.size)
print(arr2d.dtype)

arr3d = np.array([[[1,2,3,4],[5,6,7,8],[9,0,9,8]]])
print(arr3d)
print(arr3d.ndim)
print(arr3d.shape)
print(arr3d.size)
print(arr3d.dtype)


arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]], dtype=float)
print(arr3d)
#print(arr3d.ndim)
#print(arr3d.shape)
#print(arr3d.size)
# print(arr3d.dtype)
# print(arr3d[0,0,0])
# print(arr3d[0,1,2])
# print(arr3d[0,2,1])

# arr3d[0,1,1] = 500
# print(arr3d)
print(arr3d*5)

arrtest = np.array([[
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]],[1,1,1,1],[2,2,2,2],[3,3,3,3]])

print(arrtest)
print(arrtest.ndim)
print(arrtest.shape)
print(arrtest.size)
print(arrtest.dtype)

import numpy as np

arrtest = np.array([
    [ [10, 20, 30, 40],
     [90, 100, 110, 120],
     [50, 60, 70, 80]],
    [[1,1,1,1],
     [2,2,2,2],
     [3, 3, 3, 3]
    ]
])
print("Array Shape:", arrtest.shape)


arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr[1, 2])
print(arr[2, 0])
print(arr[0:2, 1:3])

