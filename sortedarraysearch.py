n=int(input())
arr=list(map(int,input().split()))
target=int(input())
def solution():
    i=0
    j=n-1
    while i<=j:
        mid=(i+j)//2
        if arr[mid]==target:
            return mid
        if arr[i]<=arr[mid]:
            if arr[i]<=target<arr[mid]:
                j=mid-1
            else:
                i=mid+1
            
        else:
            if arr[mid]<target<=arr[j]:
                i=mid+1
            else:
                j=mid-1
    return -1

            
            
        
ans = solution()
print(ans)
