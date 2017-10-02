import math
def canLaunch(numberOfShips):
    d=1
    flag=False
    t = (3 * (d ** 2) - d)/2
    print t
    while (3 * (d ** 2) - d)/2 <= numberOfShips:
        if (3 * (d ** 2) - d)/2 == numberOfShips:
            flag=True
            break
        d+=1
    return flag


# to find whether given no. is pentagonal number or not
# pentagonal number have the formula (3 * (d ** 2) - d) / 2
# I solved this challenge on codefights.com
