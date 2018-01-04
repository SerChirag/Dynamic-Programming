#Implementation in pow(2)
def LIS():

    l = len(a)
    p = [1]*l
    for i in range(l):
        for j in range(i):
            if(a[i]>a[j] and p[j]+1 > p[i]):
                p[i] = p[j]+1
                

    return p[l-1]
            


#Implementation in Log(N)
def LIS():

a = [50,3,10,7,40,80]
print LIS()
