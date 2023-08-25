import sys
input = sys.stdin.readline


def max_square(i, j, n, m, rectangle) -> int:
    max_len = 1
    extra_len = 0
    while i + extra_len < n and j + extra_len < m:
        if rectangle[i][j] == rectangle[i + extra_len][j] == rectangle[i][j + extra_len] == rectangle[i + extra_len][j + extra_len]:
            max_len = max(max_len, extra_len + 1)
        extra_len += 1

    return max_len * max_len


def solution(n, m, rectangle) -> int:
    answer = 1
    for i in range(n):
        for j in range(m):
            answer = max(answer, max_square(i, j, n, m, rectangle))

    return answer


if __name__ == '__main__':
    n, m = map(int, input().split())
    rectangle = [input().rstrip() for _ in range(n)]
    
    print(solution(n, m, rectangle))