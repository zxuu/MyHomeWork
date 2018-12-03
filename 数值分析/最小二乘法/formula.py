import matplotlib.pyplot as plt
import numpy as np
def getParameter(x,y):
    meanx = sum(x) / len(x)   #求x的平均值
    meany = sum(y) / len(y)   #求y的平均值
    xsum = 0.0
    ysum = 0.0
    for i in range(len(x)):
        xsum += (x[i] - meanx)*(y[i]-meany)
        ysum += (x[i] - meanx)**2
    a = xsum/ysum
    b = meany - a*meanx
    return a,b   #返回拟合的两个参数值
"""
Xi,Yi分别是要拟合的数据的自变量列表和因变量列表
"""
Xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
Yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])
a,b = getParameter(Xi,Yi)
print("a=",a," ","b=",b)
plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,10,1000)
y=a*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
plt.legend()
plt.show()