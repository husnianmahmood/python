import numpy as np

arr_1d = np.zeros(4)
arr_2d = np.zeros((2,3))
arr_3d = np.zeros((1,3,3))
arr_3d_2 = np.zeros((2,2,2))

print(arr_1d)
print(arr_2d)
print(arr_3d)
print(arr_3d_2)

arr_1d = np.zeros(4, dtype=int)
print(arr_1d.dtype)

arr_full = np.full(4,9)
print(arr_full)
arr_one = np.ones((2,3),dtype=int)
print(arr_one)

arr_arange = np.arange(1,9,2)
print(arr_arange)
arr_arange2 =np.arange(100,0,-10)
print(arr_arange2)

arr_linspace = np.linspace(1,7,3)
print(arr_linspace)

arr = np.random.rand(3)

print(arr)

arr_random = np.random.randint(1,5,2)
print(arr_random)
arr_random=np.random.randint(1,5,5)
print(arr_random)

arr = np.ones((4,5),dtype=int)
print(arr)
