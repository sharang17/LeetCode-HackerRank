import sys
def maxSubArray(arr):
    if len(arr)==1:
        return arr[0]
    else:
        max_sum=-sys.maxint
        curr=0
        for i in range(0,len(arr)):
            curr=max(arr[i],curr+arr[i])
            max_sum=max(max_sum,curr)
        return max_sum










arr=[-2,-1]
print maxSubArray(arr)
