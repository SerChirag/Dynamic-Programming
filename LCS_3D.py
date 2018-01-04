def LCS():

    a = [[[0 for k in range(len(s3)+1)] for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            for k in range(1,len(s3)+1):
                if(s1[i-1] == s2[j-1] == s3[k-1]):
                    a[i][j][k] = 1 + a[i-1][j-1][k-1]

                else:

                    a[i][j][k] = max(a[i-1][j][k],a[i][j-1][k],a[i][j][k-1])


    return a[len(s1)][len(s2)][len(s3)]

    
                    




s1 = "abcd1e2"
s2 = "bc12ea"
s3 = "bd1ea"
print LCS()
