import numpy as np
#获得U,L
def getUL(A_Matric):
    U = A_Matric.copy()
    L = A_Matric.copy()
    n = len(A_Matric)
    #高斯消去
    for k in range(0,n-1):
        for i in range(k+1,n): #执行下面的每一行
            factor = U[i,k]/U[k,k]
            L[i,k] = factor #把系数记录下来
            for j in range(k+1,n):
                U[i,j] = U[i,j] - factor*U[k,j]
    for i in range(0,n):
        L[i,i] = 1
        for j in range(i+1,n):
            L[i,j] = 0
    return U,L
def getD(L,B):
    return np.linalg.inv(L)*B

#高斯回带
def getX(U,D):
    n = len(U)
    Xi = [0]*n
    #首先计算出最后一个x的值
    Xi[n-1] = D[n-1,0]/U[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum = D[i,0]
        for j in range(i+1,n):
            sum -= U[i,j]*Xi[j] #每次减去等式左边的一个计算出来的常量(挪的过程)
        Xi[i] = sum/U[i,i] #计算出下一个x的值
    return Xi

if __name__ == '__main__':
    A_Matric = np.mat([[2.0,2.0,3.0],[4.0,7.0,7.0],[-2.0,4.0,5.0]],dtype = float)
    B_Matric = np.mat([3.0,1.0,-7.0],dtype = float).T
    U,L = getUL(A_Matric)
    D = getD(L,B_Matric)
    X = getX(U,D)
    print('U: ',U)
    print('L: ',L)
    print('D: ',D)
    print('X: ',X)