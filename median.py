x=[10,9,8,7,6,5,4,3,2,1]
k=7
subset=[a for a in x if a <k]
length=len(subset)
if not length%2:
    print (subset[length / 2] + subset[length / 2 - 1]) / 2.0
else:
    print subset[(length/2)]
