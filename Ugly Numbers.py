"""
In this code, we need to find the smallest number seen by 2,3,5
Since Ugly  Number array (a) stores in increasing order. Thus when multiple of X at position ix is chosen as minimum.
The next smallest number will be X*a[ix+1]


"""


def ugly(n):
    
    a = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    m2 = 2 * a[i2]
    m3 = 3 * a[i3]
    m5 = 5 * a[i5]
    for i in range(n-1):

        val = min(m2,m3,m5)
        a.append(val)
        print (m2,m3,m5)

        if(val == m2):
            i2+=1
            m2 = 2 * a[i2]
            
        if(val == m3):
            i3+=1
            m3 = 3 * a[i3]
    
            
        if(val == m5):
            i5+=1
            m5 = 5 * a[i5]
    
    return a[-1]
  

n = input()
print ugly(n)
