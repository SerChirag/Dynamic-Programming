#Cutting Rod Problem

def Cut(n):


    cut = [0]*(n+1)

    for i in range(1,n+1):

        m = values[i-1]
        for j in range(1,i):

            val = values[j-1] + cut[i-j]
            if(val > m):
                m = val

        cut[i] = m


    return cut[n]




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


values = [1, 5, 8, 9, 10, 17, 17, 20]
print Cut(8)
