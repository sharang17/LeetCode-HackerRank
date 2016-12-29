from copy import deepcopy
def twoSum(nums,target):
    #print type(nums[0]),
    #print type(target)
    test=deepcopy(nums)
    check_sorted=all(b >= a for a, b in zip(test, test[1:]))
    if check_sorted==False:
        test.sort()
        sort_flag=1
    else:
        sort_flag=0
    #print test
    i=0
    j=len(test)-1
    flag=0
    if target>0:
        while flag==0:
            if test[i]+test[j]<target:
                i=i+1
            elif test[i]+test[j]>target:
                j=j-1
            else:
                flag=1
        if sort_flag==1:
            ans_temp=[test[i],test[j]]
            vals=[nums.index(ans_temp[0]),nums.index(ans_temp[1])]
            ans=[vals[0],vals[1]]
            ans.sort()
            return ans
        else:
            ans=[i,j]
            ans.sort()
            return ans
    elif target<0:
        while flag==0:
            if test[i]+test[j]>target:
                i=i+1
            elif test[i]+test[j]<target:
                j=j-1
            else:
                flag=1
        if sort_flag==1:
            ans_temp=[test[i],test[j]]
            vals=[nums.index(ans_temp[0]),nums.index(ans_temp[1])]
            ans=[vals[0],vals[1]]
            ans.sort()
            return ans
        else:
            ans=[i,j]
            ans.sort()
            return ans
    else:
        while flag==0:
            if test[i]+test[j]<0:
                i+=1
            elif test[i]+test[j]>0:
                j-=1
            else:
                flag=1
        if sort_flag==1:
            ans_temp=[test[i],test[j]]
            vals=[nums.index(ans_temp[0]),nums.index(ans_temp[1])]
            ans=[vals[0],vals[1]]
            ans.sort()
            return ans
        else:
            ans=[i,j]
            ans.sort()
            return ans


nums=[-1,-2,-3,-4,-5]
target=-8
ans=twoSum(nums,target)
print ans
