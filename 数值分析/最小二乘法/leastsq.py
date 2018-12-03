import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

Xi = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
Yi = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])


def func(p, x):
    k, b = p

    print("k=", k, " ", "b=", b)
    return k * x + b


def error(p, x, y):
    return func(p, x) - y  # x、y都是列表，故返回值也是个列表


p0 = [100, 2]
Para = leastsq(error, p0, args=(Xi, Yi))  # 试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
a, b = Para[0]
print("k=", a, '\n', "b=", b)

plt.figure(figsize=(8, 6))
plt.scatter(Xi, Yi, color="red", label="Sample Point", linewidth=3)  # 画样本点
x = np.linspace(0, 10, 1000)
y = a * x + b
plt.plot(x, y, color="orange", label="Fitting Line", linewidth=2)  # 画拟合直线
plt.legend()
plt.show()