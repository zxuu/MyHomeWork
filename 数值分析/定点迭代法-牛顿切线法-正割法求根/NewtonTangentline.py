#用牛顿切线法求x = 3*np.exp(x)-4*np.cos(x)在1附近的根
import numpy as np
x1 = 1
def f(x):
    return 3*np.exp(x)-4*np.cos(x)
def g(x):
    return 3*np.exp(x)+4*np.sin(x)
x2 = x1 - f(x1)/g(x1) #由直线的坐标和斜率可得该直线与x轴的交点
while (x1-x2)>10**-3: #直到相邻两交点的值小于某一规定值
    x3 = x2 - f(x2)/g(x2) #求下一交点的值
    x1 = x2 #将原先的x2点作为为x1
    x2 = x3 #将下一交点的值x3作为x2
    print(x2)
print(x2) #输出根x2