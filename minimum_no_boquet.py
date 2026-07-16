blooms = list(map(int, input().split()))
m = int(input())
k = int(input())

def solution():
    # Impossible case
    if m * k > len(blooms):
        return -1

    i = 1
    j = max(blooms)

    while i < j:
        mid = (i + j) // 2

        consecutive = 0
        bouquet = 0

        for bloom in blooms:
            if bloom <= mid:
                consecutive += 1

                if consecutive == k:
                    bouquet += 1
                    consecutive = 0
            else:
                consecutive = 0

        if bouquet >= m:
            j = mid
        else:
            i = mid + 1

    return i

print(solution())
