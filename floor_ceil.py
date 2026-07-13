n = int(input())
arr = list(map(int, input().split()))
target = int(input())

def solution():
    i = 0
    j = n - 1
    floor=-1
    ceil=-1

    while i <= j:
        mid = (i + j) // 2
        if arr[mid] >= target:
            ceil= arr[mid]
            j = mid - 1
        else:
            floor=arr[mid]
            i = mid + 1
    return floor,ceil

ans = solution()
print(ans)
