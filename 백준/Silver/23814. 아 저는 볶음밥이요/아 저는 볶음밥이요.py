import sys
input = sys.stdin.readline


def solution(d, n, m, k) -> int:
    total = (n + m + k) // d
    while (n // d) + (m // d) + (k // d) != total:
        extra_n = d - n % d
        extra_m = d - m % d
        if extra_n > extra_m:
            m += extra_m
            k -= extra_m
        else:
            n += extra_n
            k -= extra_n

    return k


if __name__ == '__main__':
    d = int(input())
    n, m, k = map(int, input().split())

    print(solution(d, n, m, k))