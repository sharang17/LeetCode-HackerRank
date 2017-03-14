def rotateArray(arr,k):
    arr_new=[0]*len(arr)
    for i in range(0,len(arr)):
        if i+k<len(arr):
            arr_new[i+k]=arr[i]
        else:
            arr_new[(i+k)%n]=arr[i]
    arr=arr_new
    print arr











arr=[1,2,3,4,5,6,7]
n=len(arr)
k=3
rotateArray(arr,3)
