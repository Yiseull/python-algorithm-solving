import sys
input = sys.stdin.readline


def spread_fine_dust(r, c, A) -> None:
    tmp_A = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if A[i][j] > 4:
                a = A[i][j] // 5
                count = 0
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_x = dx + j
                    next_y = dy + i
                    if -1 < next_x < c and -1 < next_y < r and A[next_y][next_x] != -1:
                        tmp_A[next_y][next_x] += a
                        count += 1
                tmp_A[i][j] += A[i][j] - (a * count)
            else:
                tmp_A[i][j] += A[i][j]
    return tmp_A


def operate_air_purifier(r, c, A, air_purifier) -> None:
    for i in range(air_purifier - 1, 0, -1):
        A[i][0] = A[i - 1][0]
    for j in range(c - 1):
        A[0][j] = A[0][j + 1]
    for i in range(air_purifier):
        A[i][-1] = A[i + 1][-1]
    for j in range(c - 1, 1, -1):
        A[air_purifier][j] = A[air_purifier][j - 1]
    A[air_purifier][1] = 0

    for i in range(air_purifier + 2, r - 1):
        A[i][0] = A[i + 1][0]
    for j in range(c - 1):
        A[-1][j] = A[-1][j + 1]
    for i in range(r - 1, air_purifier + 1, -1):
        A[i][-1] = A[i - 1][-1]
    for j in range(c - 1, 1, -1):
        A[air_purifier + 1][j] = A[air_purifier + 1][j - 1]
    A[air_purifier + 1][1] = 0


def count_fine_dust(A) -> int:
    return sum(map(sum, A))


def solution(r, c, t, A) -> int:
    for i in range(r):
        if A[i][0] == -1:
            air_purifier = i
            break
    for _ in range(t):
        A = spread_fine_dust(r, c, A)
        operate_air_purifier(r, c, A, air_purifier)
    return count_fine_dust(A) + 2


if __name__ == '__main__':
    r, c, t = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r)]
    print(solution(r, c, t, A))