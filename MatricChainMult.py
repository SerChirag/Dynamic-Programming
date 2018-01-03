def mult(i,j):

    if(i == j):
        return 0

    m = float('inf')

    for k in range(i,j):

        count = mult(i,k) + mult(k+1,j) + a[i-1]*a[k]*a[j]
        
        if(count < m):
            m = count

    return m
    

    






a = [40,20,30,10,30]
n = len(a)-1
print mult(1,n)
