from heapq import *
import sys
input = sys.stdin.readline


def solution(m: int, n: int, l: int, positions: list, animals: list) -> int:
    animals = sorted([[min(x + y - l, x - y + l), max(y - x - l, x - y + l)] for x, y in animals])
    positions.sort()
    heap = []
    answer, i = 0, 0
    for x1, x2 in animals:
        if positions[i] < x1:
            answer += len(heap)
            heap = []
            i += 1
        if positions[i] <= x2:
            heappush(heap, x2)
    return answer + len(heap)


if __name__ == '__main__':
    m, n, l = map(int, input().split())
    positions = list(map(int, input().split()))
    animals = [list(map(int, input().split())) for _ in range(n)]
    print(solution(m, n, l, positions, animals))