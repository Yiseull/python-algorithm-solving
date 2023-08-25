import sys
input = sys.stdin.readline


def solution(n, m, rectangle) -> int:
    for extra_len in range(min(n, m) - 1, -1, -1):
        for i in range(n - extra_len):
            for j in range(m - extra_len):
                if rectangle[i][j] == rectangle[i + extra_len][j] == rectangle[i][j + extra_len] == rectangle[i + extra_len][j + extra_len]:
                    return (extra_len + 1) ** 2


if __name__ == '__main__':
    n, m = map(int, input().split())
    rectangle = [input().rstrip() for _ in range(n)]

    print(solution(n, m, rectangle))