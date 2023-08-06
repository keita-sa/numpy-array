import numpy as np

arr1 = np.array([1.0, 2.0, 3.0])

print(arr1)
print(arr1 + 1)

print(arr1.dtype)

print('----------------array2')
arr2 = np.array([1.0, 2.0, 3.0], dtype=np.float32)

print(arr2)
print(arr1 + arr2)

print(arr1 * arr2)
print(2 * arr1)

print('----------------array3')
arr3 = np.zeros([10, 10, 10], dtype=np.float32)
print(arr3.shape)
print(arr3[0])

print('----------------array4')
arr4 = np.arange(27)
print(arr4)

arr4 = arr4.reshape(3, 3, 3)
print(arr4)
print('----------------')
print(arr4[0])
print('----------------')
print(arr4[1][0])
print('----------------')
print(arr4.flatten())            # 1次元のnumpy array（平坦化）

print('----------------array5')
arr5 = np.ones([3, 3, 3])
print(arr5)

print('----------------array6')
arr6 = np.linspace(0, 10, 100)
print(arr6.shape)

print('----------------array7')
arr7 = np.random.randn(4, 4, 4)  # 正規分布に従う乱数
print(arr7)
np.random.seed(123)              # 疑似乱数の種を指定

print('----------------array8')
arr8 = np.random.randint(10, size=5)
print(arr8)


