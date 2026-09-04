import numpy as np

arr = np.array([1,2,3,4,5])
arr2 = np.array([9,8,7,6,5])

arithmetic operation
print(arr+5)
print(arr-2)
print(arr*7)
print(arr/3)
print(arr+arr2)
print(arr-arr2)
print(arr*arr2)
print(arr/arr2)


Aggregation
print(np.sum(arr))
print(np.sum(arr2))
print(np.mean(arr))
print(np.mean(arr2))
print(np.median(arr))
print(np.median(arr2))
print(np.min(arr))
print(np.min(arr2))
print(np.std(arr))
print(np.std(arr2))


axis
marks = np.array([
    [80, 70, 90],
    [60, 75, 85],
    [90, 95, 80]
])

print(np.mean(marks, axis=0))
print(np.mean(marks, axis=1))

print(np.sum(marks, axis=0))
print(np.sum(marks, axis=1))

print(np.median(marks, axis=0))
print(np.median(marks, axis=1))

print(np.std(marks, axis=0))
print(np.std(marks, axis=1))

print(np.min(marks, axis=0))
print(np.min(marks, axis=1))


reshape

marks = np.array([
    [80, 70, 90],
    [60, 75, 85],
    [90, 95, 80]
])

print(marks.shape)
print(marks.ndim)

arr = np.array([1,2,3,4,5,6])
arr2 = np.array([9,8,7,6,5,4])

print(arr.shape)
print(arr2.shape)
print(arr.reshape(2,3))
print(arr.reshape(3,2))
print(arr2.reshape(2,3))
print(arr2.reshape(3,2))

print(arr.shape)
print(arr2.shape)

boolean filtering

arr = np.array([1,2,3,4,5,6])
arr2 = np.array([9,8,7,6,5,4])

print(arr[arr>3])
print(arr2[arr2>5])
print(arr>3)
print(arr2>5)
