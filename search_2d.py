rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

target = int(input())

def solution():
    low = 0
    high = rows * cols - 1

    while low <= high:
        mid = (low + high) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:
            return True

        elif value < target:
            low = mid + 1

        else:
            high = mid - 1

    return False

print(solution())
