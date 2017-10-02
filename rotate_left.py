def rotate(a,k):
    for i in range(k):
        y=a[0]
        del a[0]
        a.append(y)
    return a

a=[]
x=int(input())
y=int(input())
for i in range(x):
    z=int(input())
    a.append(z)

print(rotate(a,y))
