def SP(s):

    p = len(s)
    e = [[0 for j in range(p)] for i in range(p)]

    for l in range(1,p+1):
        for i in range(0,p-l+1):

            j = i+l-1
            
            if(i == j):
                e[i][j] = 1
            elif(i == j-1 and s[i] == s[j]):
                e[i][j] = 2
            elif(s[i] == s[j]):
                e[i][j] = 2 + e[i+1][j-1]
            else:
                e[i][j] = max(e[i][j-1],e[i+1][j])
        


  
    return e[0][p-1]


def SPN(i,j):

    global s
    if(i == j):
        return 1
    
    if(i == j-1 and s[i] == s[j]):
        
        return 2

    if(s[i] == s[j]):
        
        return (2 + SPN(i+1,j-1))
    
    return max(SPN(i,j-1),SPN(i+1,j))



s = "GSEEKES"
a = len(s)-1
#print SPN(0,a)
print SP(s)
