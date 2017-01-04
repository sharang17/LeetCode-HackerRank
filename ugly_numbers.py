def getUgly(n):
    ugly=[0]*(n)
    ugly[0]=1
    i2=0
    i3=0
    i5=0
    m_i2=ugly[i2]*2
    m_i3=ugly[i3]*3
    m_i5=ugly[i5]*5
    for i in range(1,n):
        next_ugly=min(m_i2,m_i3,m_i5)
        ugly[i]=next_ugly
        if next_ugly==m_i2:
            i2+=1
            m_i2=ugly[i2]*2
        if next_ugly==m_i3:
            i3+=1
            m_i3=ugly[i3]*3
        if next_ugly==m_i5:
            i5+=1
            m_i5=ugly[i5]*5
    return next_ugly

n=150
print "The "+str(n)+"th Ugly Number is ", getUgly(n) 
