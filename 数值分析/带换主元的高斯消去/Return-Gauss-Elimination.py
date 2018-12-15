import numpy as np
from numpy.linalg import solve
def setMatrix():
    a_matrix = np.mat([[5.0,-1.0,1.0],[2.0,1.0,2.0],[1.0,-3.0,-4.0]],dtype = float)
    b_matrix = np.mat([8.0,5.0,-4.0],dtype = float).T
    x=solve(a_matrix,b_matrix)        #调用函数得到正确的解
    print('正确的解:',x)
    return a_matrix,b_matrix
#交换主元，把小的换到上面
def jiaohuanzhuyuan(a_matric, b_matric, xiabiao, x_matricc):
    x_matric = x_matricc
    n = len(a_matric)
    k = xiabiao
    p = k
    big = np.abs(a_matric[k,k]) #初始化第k行第k个数为最大值
    for i in range(k+1,n): #从第k+1行到最后一行检查是否有比big还要大的
        dummy = np.abs(a_matric[i,k])
        if dummy < big: #如果有则交换
            big = dummy
            p = i #并把行的下标记录下来冰赋值给p
    if p != k: #如果确实发生了交换
        for j in range(k,n): #则大的一行的所有值都要交换
            dummy2 = a_matric[p,j] #dummy2为中间变量
            a_matric[p,j] = a_matric[k,j]
            a_matric[k,j] = dummy2
        dummy3 = b_matric[p,0] #而且解也要交换
        dummyx = x_matric[p] #x1,x2,x3的位置也要交换
        b_matric[p,0] = b_matric[k,0]
        x_matric[p] = x_matric[k]
        b_matric[k,0] = dummy3
        x_matric[k] = dummyx
    return a_matric,b_matric,x_matric #返回新的参数数组和值数组
#高斯消去，消去的过程中也要交换主元
def Gauss_elimination(a_newMatric,b_newMatric,x_matricc):
    n = len(a_newMatric)
    x_matric =  x_matricc
    for k in range(0,n-1): #第一个循环和第二个循环把以后的每行的第k个数变为0
        print('交换主元前')
        print(a_newMatric,b_newMatric)
        for i in range(k+1,n): #第二个循环
            factor = a_newMatric[i,k]/a_newMatric[k,k]
            for j in range(k+1,n): #第三个循环当前行重新赋值
                a_newMatric[i,j] = a_newMatric[i,j] - factor*a_newMatric[k,j]
            b_newMatric[i,0] = b_newMatric[i,0] - factor*b_newMatric[k,0]
        #从a_newMatric[k+1,k+1]往下交换主元
        a_newMatric,b_newMatric,x_matric = jiaohuanzhuyuan(a_newMatric,b_newMatric,k+1,x_matric)
        print('交换主元后')
        print(a_newMatric,b_newMatric)
    return a_newMatric,b_newMatric,x_matric #返回新的参数数组和值数组
#高斯回带
def Gauss_Returnband(a_uppertriangle,b_uppertriangle):
    n = len(a_uppertriangle)
    Xi = [0]*n
    #首先计算出最后一个x的值
    Xi[n-1] = b_uppertriangle[n-1,0]/a_uppertriangle[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum = b_uppertriangle[i,0]
        for j in range(i+1,n):
            sum -= a_uppertriangle[i,j]*Xi[j] #每次减去等式左边的一个计算出来的常量(挪的过程)
        Xi[i] = sum/a_uppertriangle[i,i] #计算出下一个x的值
    return Xi #返回解
if __name__ == '__main__':
    x_matric = [1,2,3] #记录x1,x2,x3的顺序
    a,b = setMatrix()
    print('交换前')
    print(a,b)
    a,b,x_matric = jiaohuanzhuyuan(a,b,0,x_matric)
    print('交换后')
    print(a,b)
    a_uppertriangle,b_uppertriangle,x_matric = Gauss_elimination(a,b,x_matric)
    print('三角矩阵,只有上三角有用')
    print(a_uppertriangle)
    print(b_uppertriangle)
    X = Gauss_Returnband(a_uppertriangle,b_uppertriangle)
    print(X)
    print('x1,x2,x3的位置分别在：',x_matric)
    print('调回到原来的顺序后所以x1,x2,x3的值分别为',)
    for i in range(0,3):
        print('x',x_matric[i],'的值为:',X[x_matric[i]-1])