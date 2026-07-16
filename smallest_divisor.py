from math import ceil
nums=list(map(int,input().split()))
threshold=int(input())
def solution():
    i=1
    j=max(nums)
    
    while i<j:
        sum=0
        mid=(i+j)//2
        for num in nums:
            sum+=ceil(num/mid)
        if sum<=threshold:
            j=mid
        else:
            i=mid+1
    return i
            
print(solution())
