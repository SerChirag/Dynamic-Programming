def edit(str1,str2):

    edit = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]

    count = 0
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if(str1[i-1] == str2[j-1]):
                edit[i][j] = edit[i-1][j-1] + 1
            else:
                edit[i][j] = max(edit[i][j-1],edit[i-1][j])

    return edit[len(str1)][len(str2)]
                
                



str1 = "ABCDGH"
str2 = "AEDFHR"
print edit(str1,str2)
