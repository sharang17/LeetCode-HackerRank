def longestIncSub(arr):
    n=len(arr)
    lis=[1]*n
    #print lis
    print arr
    print lis
    for i in xrange(1,n):
        for j in xrange(0,i):
            if arr[i]>arr[j] and lis[i]<lis[j]+1:
                lis[i]=lis[j]+1
                print lis
    maximum=0
    for i in range(1,n):
        maximum=max(maximum,lis[i])
    print lis
    return maximum




arr = [10, 22, 9, 33, 21, 50, 41, 60]

length=longestIncSub(arr)
#print length
