import math
def f(p,b):
    if not b:
        return -1
    vp=1
    for i in p:
        vp*=i
    minp=min(p)
    minb=[]
    for i in b:
        minb.append(min(i))
    c=sum(map(ord,p))
    print(c)

    
print(f([4,1,5],[[4,2,5],[4,3,5]]))
        
