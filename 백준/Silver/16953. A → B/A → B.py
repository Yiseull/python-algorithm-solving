import sys
input = sys.stdin.readline


def solution(a, b) -> int:
    answer = 1
    while a < b:
        if b % 2 == 0:
            b //= 2
        elif b % 10 == 1:
            b //= 10
        else:
            return -1
        answer += 1

    return answer if a == b else -1


if __name__ == '__main__':
    a, b = map(int, input().split())

    print(solution(a, b))