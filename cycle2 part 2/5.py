import numpy as np
A=np.array([[1,2,3],[2,4,5],[3,5,8]])
B=np.array([[0,2,4],[-2,0,3],[-4,-3,0]])
AT=A.transpose()
comparison = A == AT
equal_arrays = comparison.all()
print(equal_arrays)
m=(B.transpose() == -B).all()
print(m)
