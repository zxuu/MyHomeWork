
# coding: utf-8

# In[29]:


#x0=1,x1=4,x2=6 f(x0)=0,f(x1)=1.3863,f(x2)=1.7918
import matplotlib.pyplot as plt
import numpy as np
Xi=[1,4,6]
Yi=[0,1.3863,1.7918]
def getY(x):
    total = 0
    for i in range(len(Xi)):
        fenzi = 1
        fenmu = 1
        for j in range(len(Xi)):
            if i == j:
                continue
            fenzi = fenzi*(x-Xi[j])
            fenmu = fenmu*(Xi[i]-Xi[j])
        total = total + fenzi*Yi[i]/fenmu
    return total
    #print("f(x)在x=",x,"处的值为：",total)
if __name__ == '__main__':
    print("f(x)在x=2处的值为：",getY(2))
    x = np.arange(-5, 5, 0.2)
    y = getY(x)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x, y)
    plt.show()

