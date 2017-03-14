

def findMaxConsecutiveOnes(nums):
    count=0
    ans=0
    for num in nums:
        if num==1:
            count+=1
            ans=max(count,ans)
        else:
            count=0
    return ans
    
nums=[1,1,0,1,1,1]
findMaxConsecutiveOnes(nums)
