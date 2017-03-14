n,k=4,3

a=[1,7,2,4]

L=[0]*k
for x in a:
    L[x % k ]+=1
res=0
for i in range(k/2+1):
    if i==0 or i==k*2:
        res+=bool(L[i])
    else:
        res+=max(L[i],L[k-i])
print res
