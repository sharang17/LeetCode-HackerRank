
import collections

def countPairs(nums,k):
    if k>0:
        return len(set(nums) and set(n+k for n in set(nums)))
    elif k==0:
        return sum(v>1 for v in collections.Counter(nums).values())
    else:
        return 0



nums=[1, 3, 1, 5, 4]
k=0
print countPairs(nums,k)
