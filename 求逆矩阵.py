#%%
import numpy as np

m,n = input("输出矩阵的行数和列数：").split()
m = int(m)
n = int(n)

A = np.zeros((m,n))
for i in range(m):
    for j in range(n):
        temp = input("输入第{}行第{}列的元素：".format(i+1,j+1))
        if temp == "":
            A[i][j] = 0
        else:
            A[i][j] = float(temp)

print("矩阵A为：{}".format(A))

print("矩阵A的逆矩阵为：{}".format(np.linalg.inv(A)))

flag = int(input("是否计算相似矩阵"))
if flag == 1:
    B = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            temp = input("输入第{}行第{}列的元素：".format(i+1,j+1))
            if temp == "":
                B[i][j] = 0
            else:
                B[i][j] = float(temp)
    print("矩阵B为：{}".format(B))
    print("矩阵A和B的相似矩阵为：{}".format(np.linalg.inv(A)@B@A))