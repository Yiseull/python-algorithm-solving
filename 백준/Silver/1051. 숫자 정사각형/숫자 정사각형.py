import sys
input = sys.stdin.readline


def solution(n, m, rectangle) -> int:
    answer = 1
    for i in range(n):
        for j in range(m):
            for extra_len in range(1, min(n - i, m - j)):
                if rectangle[i][j] == rectangle[i + extra_len][j] == rectangle[i][j + extra_len] == rectangle[i + extra_len][j + extra_len]:
                    answer = max(answer, pow(extra_len + 1, 2))

    return answer


if __name__ == '__main__':
    n, m = map(int, input().split())
    rectangle = [input().rstrip() for _ in range(n)]

    print(solution(n, m, rectangle))