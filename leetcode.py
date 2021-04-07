
def twosum(l1, l2):
    if 1 <= len(l1) <=100 and 1 <=len(l2)<=100:
        x1 = ''
        x2 = ''
        for i in l1:
            if 0 <= i <= 9:
                x1 += str(i)
        for i in l2:
            if 0 <= i <= 9:
                x2 +=str(i)
        x3 = int(x1) + int(x2)
        x3 = list(str(x3))
    
        return x3[::-1]

l1 = [2,4,3]
l2 = [5,6,4]
# print(twosum(l1, l2))
print(2147483647**200)
a = 2147483647
b = [2,0,0]
x = 1198
from math import sqrt
print(sqrt(a))





