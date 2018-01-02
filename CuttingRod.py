#Cutting Rod Problem


def CutNaive(n):

    if(n == 0):
        return 0
    else:
        m = values[n-1]
        for i in range(1,n+1):
            
            val = values[i-1] + Cut(n-i)
            if(val > m):
                m = val

        return m


values = [3,5,8,9,10,17,17,20]
print CutNaive(8)
