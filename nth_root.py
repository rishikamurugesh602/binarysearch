n = int(input())
m = int(input())

def solution():
    i = 1
    j = m

    while i <= j:
        mid = (i + j) // 2
        val = mid ** n

        if val == m:
            return mid
        elif val < m:
            i = mid + 1
        else:
            j = mid - 1

    return -1

print(solution())
