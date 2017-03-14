
def find_nonrep(string):
    order=[]
    counts={}
    for s in string:
        if s in counts:
            counts[s]+=1
        else:
            counts[s]=1
            order.append(s)
    for s in order:
        if counts[s]==1:
            return s
    return None

def count_occurence(string,ch):
    counts={}
    for s in string:
        if s in counts:
            counts[s]+=1
        else:
            counts[s]=1
    if ch not in counts:
        return None
    else:
        count=counts.get(ch)
        return count





string='aabccbdcbe'
#print find_nonrep(string)
print count_occurence(string,'b')
