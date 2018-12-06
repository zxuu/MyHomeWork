#x0=0,x1=1,x2=2,x3=4 f(x0)=3,f(x1)=6,f(x2)=11,f(x3)=51
Xi=[0,1,2,4]
Yi=[3,6,11,51]
myydict={0:3,1:6,2:11,4:51}
mydict={4:51,2:11,1:6,0:3}
def getB(mydict): #递归求解
    n = len(mydict)
    if(n == 2):
        return (list(mydict.values())[0]-list(mydict.values())[1])/(list(mydict)[0]-list(mydict)[1])
    dict_slice = lambda mydict, start, end: { k:mydict[k] for k in list(mydict.keys())[start:end] }
    mydict1 = dict_slice(mydict, 0, n-1) #f(0,...n-1)
    mydict2 = dict_slice(mydict, 1, n) #f(1,...n)
    return (getB(mydict1)-getB(mydict2))/(list(mydict)[0]-list(mydict)[n-1])
if __name__ =='__main__':
    n=len(mydict)
    b=[0]*n
    print("b 0 =",list(mydict.values())[n-1])
    b[0]=list(mydict.values())[n-1]
    j=1
    for i in range(n-2,-1,-1):
        dict_slice = lambda mydict, start, end: { k:mydict[k] for k in list(mydict.keys())[start:end] }
        l = dict_slice(mydict, i, n)
        bi=getB(l)
        b[j]=bi
        print("b",j,"=",bi)
        j+=1
    print("b参数数组为：",b)
    print("赵旭1607094242")