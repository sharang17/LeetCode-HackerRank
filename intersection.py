def intersection(nums1,nums2):
    set1=set(nums1)
    set2=set(nums2)
    inter=set1 & set2
    inter=list(inter)
    return inter







nums1=[1, 2, 2, 1]
nums2=[2,2]
print intersection(nums1,nums2)
