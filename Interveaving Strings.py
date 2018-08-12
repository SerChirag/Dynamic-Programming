a = "freddie"
b = "david"
c = "fdredavdiide"
m = []
for i in range(len(a)+1):
    f = []
    for j in range(len(b)+1):
        f.append(0)
    m.append(f)
if(len(c) == len(a)+len(b)):
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if(i == 0 and j == 0):
                m[0][0] = 1
            elif(i == 0):
                if(c[j-1] == b[j-1]):
                    m[0][j] = 1
            elif(j == 0):
                if(c[i-1] == a[i-1]):
                    m[i][0] = 1
            else:
                if(c[i+j-1] == a[i-1] or c[i+j-1] == b[j-1]):
                    m[i][j] = m[i-1][j] or m[i][j-1]

    for i in  range(len(m)):
        for j in  range(len(m[0])):
            print m[i][j],
        print
    if(m[-1][-1] == 1):
        print "Yes"
    else:
        print "No"
else:
    print "No"
