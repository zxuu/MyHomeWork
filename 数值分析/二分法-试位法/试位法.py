import numpy as np
#试位法
a = 0.1
b = 2
def f(x):
    return 1-x-np.sin(x)
i = 0
while 1:
    #c为连线与x轴的交点
    # c-a     \f(a)\
    #----- = --------
    # b-c     \f(b)\
    c = (a*abs(b) + b*abs(f(a)))/(abs(f(a)) + abs(b))
    #试位300次
    if i == 300:
        print(c)
        break
    #交点不为零点
    elif f(c) != 0:
        #交点在零点的右边
        if f(a)*f(c) < 0:
            #交点作为区间右边界
            b = c
        #交点在零点的左边
        else:
            #交点作为零点左边界
            a = c
    else:
        print(c)
        break
    i += 1