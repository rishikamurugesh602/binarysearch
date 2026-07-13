n=int(input())
arr=list(map(int,input().split()))
target=int(input())
def solution():
    i=0
    j=n-1
    ans=n
    while i<=j:
        mid=(i+j)//2
       
        if arr[mid]>target:
            ans=mid
            j=mid-1
        else:
            i=mid+1
    return ans

            
            
        
ans = solution()
print(ans)
