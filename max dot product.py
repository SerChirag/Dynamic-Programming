#https://practice.geeksforgeeks.org/problems/maximize-dot-product/0#ExpectOP

t = input()
for q in range(int(t)):
    c = input()
    a = input().split()
    b = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(b)):
        b[i] = int(b[i])
    m = []
    for i in range(len(b)+1): #shorter array first 
        c = []
        for j in range(len(a)+1): 
            c.append(0)
        m.append(c)
    for i in range(1,len(b)+1):
        for j in range(i,len(a)+1): #notice j goes from i to len(a)
            m[i][j] = max(m[i][j-1],m[i-1][j-1]+b[i-1]*a[j-1]) #either let previous element have it or you take it
            
    
    print(m[-1][-1])
            
