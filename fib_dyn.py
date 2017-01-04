def fib_topdown(n,lookup):
    if n==1 or n==0:
        lookup[n]=n
    if lookup[n] is None:
        lookup[n]=fib_topdown(n-1,lookup)+fib_topdown(n-2,lookup)
    return lookup[n]

def fib_bottomup(n):
    fib=[0]*(n+1)

    fib[1]=1

    for i in xrange(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]




    
n=4
lookup=[None]*(101)
print "The "+str(n)+"th Fibonacci Number(Top Down) is ", fib_topdown(n,lookup)
print "The "+str(n)+"th Fibonacci Number(BottomUp) is ", fib_bottomup(n)
