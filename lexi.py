# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def lexi_greater(string):
    i=len(string)-2
    while not(i<0 or string[i] < string[i+1]):
        i-=1
    if i<0:
        print "no answer"
    else:
        j=len(string)-1
        while not(string[j] > string[i]):
            j-=1
        string=list(string)
        string[i],string[j]=string[j],string[i]
        string[i+1:]=reversed(string[i+1:])
        string=''.join(str(x) for x in string)
        print string



inp=sys.stdin.readlines()
inp=[i.strip("\n") for i in inp]
inp.pop(0)
for string in inp:
    lexi_greater(string)
