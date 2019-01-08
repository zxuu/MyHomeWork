
# coding: utf-8

# In[25]:


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 4, 0.1)
y = -2*x**3+12*x**2-20*x+8.5
plt.title("y=x**3-3*x**2+2*x+3")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
plt.show()


# In[34]:


#######欧拉法#########
import matplotlib.pyplot as plt
import numpy as np
def G(x):
    return -2*x**3+12*x**2-20*x+8.5
a = 0
b = 4
x1 = a
x2 = a
h = 0.2
y = [1]
x = [0]
if __name__ == '__main__':
    i = 0
    
    while(x[i]<b):
        y.append(y[i] + G(x[i])*h)
        x.append(x[i] + h)
        i += 1
    plt.title("g(x)=-2*x**3+12*x**2-20*x+8.5")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x, y,label='欧拉法')
#     plt.show()
    x_real = np.arange(0, 4, 0.1)
    y_real = -0.5*x_real**4+4*x_real**3-10*x_real**2+8.5*x_real+1
#     plt.title("y=x**3-3*x**2+2*x+3")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.grid()
    plt.plot(x_real, y_real,label='原函数')
    plt.legend(['欧拉法','原函数'])
    plt.legend()
    plt.show()
    print('1607094242赵旭')

