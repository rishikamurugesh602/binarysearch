n=int(input())
arr=list(map(int,input().split()))
target=int(input())
def solution():
    
    i=0
    j=n-1
    first=-1
    last=-1

    while i<=j:
        mid=(i+j)//2
        if arr[mid]==target:
            first=mid
            j=mid-1
        elif arr[mid]>target:
            j=mid-1
        else:
            i=mid+1
   
    i=0
    j=n-1
    while i<=j:
        mid=(i+j)//2
        if arr[mid]==target:
            last=mid
            i=mid+1
        elif arr[mid]>target:
            j=mid-1
        else:
            i=mid+1
    return first,last
ans=solution()
print(ans)
