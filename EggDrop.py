			if(i == j):
                e[i][j] = 1
            elif(i == j-1 and s[i] == s[j]):
                e[i][j] = 2
            elif(s[i] == s[j]):
                e[i][j] = 2 + e[i+1][j-1]
            else:
                e[i][j] = max(e[i][j-1],e[i+1][j])
        