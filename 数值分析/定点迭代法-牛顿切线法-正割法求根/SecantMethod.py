#用正割法求x = 3*np.exp(x)-4*np.cos(x)在1附近的根
import numpy as np
x1 = 1 #初始两点选择1和0.8
x2 = 0.8
def f(x):
    return 3*np.exp(x)-4*np.cos(x)
x3 = x2-((f(x2)*(x1-x2))/(f(x1)-f(x2)))#由两点式求出直线与x轴交点
while (x1-x2)>10**(-3): #直到相邻两交点的值小于某一规定值
    x3 = x2-((f(x2)*(x1-x2))/(f(x1)-f(x2))) #递推下一交点
    x1 = x2 #将原先的x2点作为为x1
    x2 = x3 #将下一交点的值x3作为x2
    print(x2)