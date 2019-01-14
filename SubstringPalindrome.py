def SP(s):
    p = len(s)
    e = [[0 for j in range(p)] for i in range(p)]
    maxi = 1
    for l in range(1,p+1):
        for i in range(0,p-l+1):
            j = i+l-1
            if(i == j):
                e[i][j] = 1
            elif(i == j-1 and s[i] == s[j]):
                e[i][j] = 1
                crap = j-i+1
                if(crap>maxi):
                    maxi = crap
                
            elif(s[i] == s[j]):
                e[i][j] = e[i+1][j-1]
                if(e[i+1][j-1] == 1):
                    crap = j-i+1
                    if(crap>maxi):
                        maxi = crap
            else:
                e[i][j] = 0
    return maxi

s = "qwertxiggixvbn"
a = len(s)-1
#print SPN(0,a)
print SP(s)
