import sys
input = sys.stdin.readline


def solution(n, buildings) -> int:
    answer = [0] * n
    for i in range(n):
        count = 0
        slope, pre_slope = 0, int(1e9)
        for j in range(i - 1, -1, -1):
            slope = (buildings[j] - buildings[i]) / (j - i)
            if slope < pre_slope:
                count += 1
                pre_slope = slope
        slope, pre_slope = 0, int(-1e9)
        for j in range(i + 1, n):
            slope = (buildings[j] - buildings[i]) / (j - i)
            if slope > pre_slope:
                count += 1
                pre_slope = slope
        answer[i] = count

    return max(answer)


if __name__ == '__main__':
    n = int(input())
    buildings = list(map(int, input().split()))
    print(solution(n, buildings))