def mergesort(nums1,nums2):
    if len(nums1)==0 and len(nums2)==0:
        return -1
    if len(nums1)!=0 and len(nums2)==0:
        return nums1
    if len(nums1)==0 and len(nums2)!=0:
        return nums2
    i=0
    j=0
    nums_sorted=[]
    while i<=len(nums1)-1 and j<=len(nums2)-1:
        if nums1[i]<nums2[j]:
            nums_sorted.append(nums1[i])
            #print nums_sorted
            i+=1
        elif nums2[j]<nums1[i]:
            nums_sorted.append(nums2[j])
            #print nums_sorted
            j+=1
    if i>=len(nums1):
        for k in range(j,len(nums2)):
            nums_sorted.append(nums2[k])
            
    if j>=len(nums2):
        for k in range(i,len(nums1)):
            nums_sorted.append(nums1[k])
    return nums_sorted
    


def findMedianSortedArrays(nums1,nums2):
    merged_array=mergesort(nums1,nums2)
    if len(merged_array)%2:
        median=merged_array[len(merged_array)/2]
    else:
        median=(merged_array[len(merged_array)/ 2] + merged_array[len(merged_array)/2- 1]) / 2.0
    return median



nums1=[1,4,11,13]
nums2=[3,6,7,10,22,25]
median=findMedianSortedArrays(nums1,nums2)
print median

