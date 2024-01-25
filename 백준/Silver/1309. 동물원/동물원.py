import sys
input = sys.stdin.readline


def solution(n: int) -> int:
        a, b, c = 1, 1, 1
        for i in range(n - 1):
            a, b, c = a + b + c, a + c, a + b

        return (a + b + c) % 9901


if __name__ == '__main__':
    n = int(input())
    print(solution(n))