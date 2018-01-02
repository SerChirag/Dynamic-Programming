def KnapSack(W,n):

    K = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if(i==0 or j==0):
                K[i][j] = 0
            elif(weight[i-1] <= j):
                K[i][j] = max(K[i-1][j], value[i-1] + K[i-1][j-weight[i-1]])
                
            else:

                K[i][j] = K[i-1][j]

    for i in range(n+1):
        for j in range(W+1):
            print K[i][j],
        print

    return K[n][W]

    


def KnapSackNaive(W,n):

    if(n==0 or W==0):
        return 0
    
    elif(weight[n-1] > W):
        return KnapSack(W,n-1)
        
    else:
        return max(KnapSack(W,n-1), value[n-1] + KnapSack(W-weight[n-1],n-1))
        
    

value = [60,100,120]
weight = [10,20,30]
W = 50
print KnapSack(W,3)
