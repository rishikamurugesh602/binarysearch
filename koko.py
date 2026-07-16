from math import ceil
piles=list(map(int,input().split()))
hours=int(input())
def solution():
    i=1
    j=max(piles)
    total=0
    while i<j:
        mid=(i+j)//2
        total=0
        for pile in piles:
    
            total+=ceil(pile/mid)
        if total<=hours:
            j=mid
        else:
            i=mid+1
    return i
    
        
                
        

print(solution())
