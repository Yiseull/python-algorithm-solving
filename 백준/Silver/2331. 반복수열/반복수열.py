import sys
input = sys.stdin.readline


def calculate_dn(pre, p) -> int:
    dn = 0
    while pre != 0:
        num, pre = pre % 10, pre // 10
        dn += pow(num, p)

    return dn


def solution(a, p) -> int:
    pre = a
    arr = [a]
    arr_set = set([a])
    while 1:
        dn = calculate_dn(pre, p)
        if dn in arr_set:
            return arr.index(dn)
        arr.append(dn)
        arr_set.add(dn)
        pre = dn


if __name__ == '__main__':
    a, p = map(int, input().split())
    print(solution(a, p))