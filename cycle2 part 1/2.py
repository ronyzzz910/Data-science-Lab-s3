import numpy as np
x=np.array([[3+2j,4+3j,5+3j],[6+6j,7+8j,8+5j]])
print(x)
print("Number of Rows and Columns:",x.shape)
print("Reshaped matrix is:")
print(x.reshape(3,2))
print("Dimensions:",x.ndim)
