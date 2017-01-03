# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

def createLL(l1,l2):
    if len(l1)>1:
        l1_node=ListNode(l1[0])
        l1_head=l1_node
        for i in range(1,len(l1)):
            l1_temp=ListNode(l1[i])
            l1_node.next=l1_temp
            l1_node=l1_node.next
    else:
        l1_node=ListNode(l1[0])
        l1_head=l1_node
    if len(l2)>1:
        l2_node=ListNode(l2[0])
        l2_head=l2_node
        for i in range(1,len(l2)):
            l2_temp=ListNode(l2[i])
            l2_node.next=l2_temp
            l2_node=l2_node.next
    else:
        l2_node=ListNode(l2[0])
        l2_head=l2_node
    nodes=[l1_head,l2_head]
    return nodes
    

def addTwoNumbers(l1,l2):
    l1_sum=""
    l2_sum=""
    while l2:
        l2_sum+=str(l2.val)
        l2=l2.next
    l2_sum=l2_sum[::-1]
    while l1:
        l1_sum+=str(l1.val)
        l1=l1.next
    l1_sum=l1_sum[::-1]
    l1_int=int(l1_sum)
    l2_int=int(l2_sum)
    l3_sum=str(l1_int+l2_int)
    l3_node=l3_sum[::-1]
    l3=ListNode(int(l3_node[0]))
    l3_head=l3
    for i in range(1,len(l3_node)):
        l3_temp=ListNode(int(l3_node[i]))
        l3.next=l3_temp
        l3=l3.next
    l3=l3_head
    while l3:
        print l3.val,
        l3=l3.next
    return l3_head


  
l1_list=[1,8]
l2_list=[0]

nodes=createLL(l1_list,l2_list)
l1=nodes[0]
l2=nodes[1]

l3=addTwoNumbers(l1,l2)
while l3:
    print l3.val,
    l3=l3.next



    
