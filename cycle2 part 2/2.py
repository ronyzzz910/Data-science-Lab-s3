import numpy as np 
arr1 =np.array([[1, 2, 3],[3,2,4],[2,2,1]])
print(arr1)
print(pow(arr1, 3))
print(np.multiply(arr1,(arr1*arr1)))
print(arr1*arr1*arr1)
print(arr1**3)

b = np.identity(3, dtype = int)
print("Identity matrix:\n", b)

out = np.power(arr1, arr1)
print("each element of the matrix to different powers:\n",out)

x = np.arange(1,10).reshape(3,3)
y = np.arange(11,20).reshape(3,3)
print("perform the operation X^2 +2Y: \n",np.add((np.power(x,2)),(np.multiply(y,2))))