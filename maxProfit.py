def maxProfit(prices):
    if all(j<i for i,j in zip(prices,prices[1:])):
        print "Enter"
        return 0
    else:
        max_diff=0
        curr_diff=0
        for i in range(0,len(prices)-1):
            if i<len(prices)-2:
                if prices[i]>max(prices[i+1:]):
                    continue
                else:
                    curr_diff=max(prices[i+1:])-prices[i]
                    max_diff=max(curr_diff,max_diff)
            else:
                if prices[i]<prices[i+1]:
                    curr_diff=prices[i+1]-prices[i]
                    max_diff=max(curr_diff,max_diff)
                else:
                    continue
        return max_diff





prices=[1,2]
print maxProfit(prices)
