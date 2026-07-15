n=int(input())
arr=list(map(int,input().split()))
def solution():
    i=0
    j=len(arr)-1
    minn=float('inf')
    while i<j:
        mid=(i+j)//2
        if arr[i]<=arr[j]:
            return arr[i]
        else:
            if arr[mid]>=arr[j]:
                i=mid+1
            else:
                j=mid
    return arr[i]
            
ans=solution()
print(ans)
    
