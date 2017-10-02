def firstDuplicate(a):
    x=[y for y in a if a.count(y)>1]
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            return x[i]
    else:
        return -1
