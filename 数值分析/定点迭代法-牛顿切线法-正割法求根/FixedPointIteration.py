import numpy as np
#用定点迭代法求x = sqrt(2*x(i))在1.2附近的根
x1 = 1.2
def f(x):
    #X(i+1) = sqrt(2*X(i))
    return (2*x)**0.5
y1 = x1
y2 = f(x1)
#直到误差小于十的负三次方停止迭代
while abs(y2-y1)>10**(-3):
    x2 = y2
    y1 = x2
    y2 = f(x2)
    print(x2)
print(x2)