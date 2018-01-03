def SP(s):

    l = [[0 for j in range(s+1)] for i in range(s+1)]
    for i in range(s):
        for j in range(s):

            if(i == j):
                l[i][j] = 1

            elif(i == j-1 and s[i] == s[j]):
                l[i][j] = 2

            elif(s[i] == s[j]):
                l[i][j] = 2 + l[i+1][j-1]

            
                

    global s
    if(i == j):
        return 1
    
    if(i == j-1 and s[i] == s[j]):
        
        return 2

    if(s[i] == s[j]):
        
        return (2 + SPN(i+1,j-1))


    
    return max(SPN(i,j-1),SPN(i+1,j))


def SPN(i,j):

    global s
    if(i == j):
        return 1
    
    if(i == j-1 and s[i] == s[j]):
        
        return 2

    if(s[i] == s[j]):
        
        return (2 + SPN(i+1,j-1))
    
    return max(SPN(i,j-1),SPN(i+1,j))



s = "geeks"
a = len(s)-1
#print SPN(0,a)
print SP(a)
