
def permutations(data):
    if len(data)==0:
        return []
    if len(data)==1:
        return [data]
    l=[]
    for i in range(len(data)):
        m=data[i]
        remList=data[:i]+data[i+1:]
        for p in permutations(remList):
            l.append([m] + p)
    return l






data=list('kia')
for p in permutations(data):
    print p
