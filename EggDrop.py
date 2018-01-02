def EggDrop(n,k):

    egg = [[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(1,n+1):
        egg[i][1] = 1

    for i in range(1,k+1):
        egg[1][i] = i

    for i in range(2,n+1):
        for j in range(2,k+1):

            m = float('inf')
            for p in range(1,k+1):
                val = 1 + max(egg[i-1][p-1],egg[i][j-p])
                if(val<m):
                    m = val 

            egg[i][j] = m
            
    return egg[n][k]
    
def EggDropNaive(n,k):

    if(n==0 or k==0):
        return 0
    if(n==1):
        return k
    m = float('inf')
    for i in range(1,k+1):

        val = max(EggDrop(n-1,i-1),EggDrop(n,k-i))
        if(val<m):
            m = val
    return m+1
        
n = 2
k = 10
print EggDrop(n,k)
