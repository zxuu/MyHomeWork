#二分法
#函数的根大致在（0,2）之间
import numpy as np
a = 0.1
b = 2
def f(x):
    #函数
    return 1-x-np.sin(x)
while 1:
    c = (a+b)/2
    #判断是否满足终止条件（当真实值误差低于一个给定的值终止）
    if (b-a) < 0.5*10**(-4):
        print(c)
        break
    #判断中值是否为零点
    elif f(c) != 0:
        #零点在中值的左边
        if f(a)*f(c) < 0:
            #中值作为区间右边界
            b = c
        #零点在中值的右边
        else:
            #中值作为区间左边界
            a = c
    else:
        print(c)
        break