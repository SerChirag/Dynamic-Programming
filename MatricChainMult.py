def mult(n):

    edit = [[0 for j in range(n+1)] for i in range(n+1)]

    for l in range(2,n):
        for i in range(1,n-l+1):

            j = i+l-1
            m = float('inf')

            for k in range(i,j):

                count = edit[i][k] + edit[k+1][j] + a[i-1]*a[k]*a[j]
                if(count < m):
                    m = count

            edit[i][j] = m

    return edit[1][n-1]

    
def multN(i,j):

    if(i == j):
        return 0

    m = float('inf')

    for k in range(i,j):

        count = mult(i,k) + mult(k+1,j) + a[i-1]*a[k]*a[j]
        
        if(count < m):
            m = count

    return m
    


a = [40,20,30,10,30]
n = len(a)
print mult(n)
