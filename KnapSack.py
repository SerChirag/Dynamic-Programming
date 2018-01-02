def KnapSack(W,n):

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
