def longestUniqueSubString(string):
    n=len(string)
    max_char=256
    cur_len=1
    max_len=1
    prev_index=0
    visited=[-1]*max_char
    visited[ord(string[0])]=0
    for i in range(1,n):
        prev_index=visited[ord(string[i])]
        if prev_index==-1 or (i-cur_len > prev_index):
            cur_len+=1
        else:
            if cur_len > max_len:
                max_len=cur_len
            cur_len=i-prev_index
        visited[ord(string[i])]=i

    if cur_len > max_len:
        max_len=cur_len
    return max_len
        
        






string = "ABDEFGABEF"
length=longestUniqueSubString(string)
print length
