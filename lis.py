global max_lis_length # stores the final LIS
 
# Recursive implementation for calculating the LIS
def _lis(arr, n):
    # Following declaration is needed to allow modification
    # of the global copy of max_lis_length in _lis()
    global max_lis_length
 
    # Base Case
    if n == 1:
        return 1
 
    current_lis_length = 1
 
    for i in xrange(0, n-1):
        # Recursively calculate the length of the LIS
        # ending at arr[i]
        subproblem_lis_length = _lis(arr, i+1)
 
        # Check if appending arr[n-1] to the LIS
        # ending at arr[i] gives us an LIS ending at
        # arr[n-1] which is longer than the previously
        # calculated LIS ending at arr[n-1]
        if arr[i] < arr[n-1] and \
            current_lis_length < (1+subproblem_lis_length):
            current_lis_length = (1+subproblem_lis_length)
 
    # Check if currently calculated LIS ending at
    # arr[n-1] is longer than the previously calculated
    # LIS and update max_lis_length accordingly
    if (max_lis_length < current_lis_length):
        max_lis_length = current_lis_length
 
    return current_lis_length
 
# The wrapper function for _lis()
def lis(arr, n):
 
    # Following declaration is needed to allow modification
    # of the global copy of max_lis_length in lis()
    global max_lis_length
 
    max_lis_length = 1 # stores the final LIS
 
    # max_lis_length is declared global at the top
    # so that it can maintain its value
    # between the recursive calls of _lis()
    _lis(arr , n)
 
    return max_lis_length

arr=[1,3,7,8,5,11,21,4,36]
n=lis(arr,len(arr))
print n
