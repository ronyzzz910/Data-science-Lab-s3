import numpy as np
x = np.array([[1,2,3,4,], [5,6,7,8],[9,10,11,12], [13, 14, 15,16]])
print(x)
print("Display all elements excluding the first row")
print(x[1:])

print("Display all elements excluding the last column")
print(x[:, :3])

print("Display the elements of 2 nd and 3 rd column")
print(x[:, 1:3])

print("Display the elements of 1 st and 2 nd column in 2 nd and 3 rd row")
print(x[1:3, :2])


print("Display 2 nd and 3 rd element of 1 st row")
print(x[0,1])
print(x[0,2])


