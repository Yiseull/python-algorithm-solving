import sys
input = sys.stdin.readline


def dfs(index, n, a, operation, result) -> None:
    if index == n:
        global _min, _max
        _min = min(_min, result)
        _max = max(_max, result)
        return

    for i in range(4):
        result_copy = result
        if operation[i] > 0:
            operation[i] -= 1
            if i == 0:
                result_copy += a[index]
            elif i == 1:
                result_copy -= a[index]
            elif i == 2:
                result_copy *= a[index]
            elif result < 0:
                result_copy *= -1
                result_copy //= a[index]
                result_copy *= -1
            else:
                result_copy //= a[index]
            dfs(index + 1, n, a, operation, result_copy)
            operation[i] += 1


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    operation = list(map(int, input().split()))
    _min, _max = int(1e9), int(1e9) * -1
    dfs(1, n, a, operation, a[0])
    print(_max)
    print(_min)