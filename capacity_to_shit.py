from math import ceil
weights=list(map(int,input().split()))
days=int(input())
def solution(weights,days):
    i=max(weights)
    j=sum(weights)
    while i<j:
        mid=(i+j)//2
        count_days=1
        current=0
        for weight in weights:
            if current+weight<=mid:
                current+=weight
            else:
                count_days+=1
                current=weight
        if count_days<=days:
            j=mid
        else:
            i=mid+1
    return i
print(solution(weights,days))
