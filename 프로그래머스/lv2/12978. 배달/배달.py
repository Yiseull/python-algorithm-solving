from heapq import *


def dijkstra(n, k, towns, start) -> int:
    delivery_towns = set()
    heap = []
    heappush(heap, (0, start))
    distance = [500000] * (n + 1)
    distance[start] = 0
    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue
        for town, road in towns[now]:
            cost = dist + road
            if distance[town] > cost:
                distance[town] = cost
                heappush(heap, (cost, town))
                if distance[town] <= k:
                    delivery_towns.add(town)
    return len(delivery_towns) + 1


def solution(n, roads, k) -> int:
    towns = [[] for _ in range(n + 1)]
    for town1, town2, road in roads:
        towns[town1].append((town2, road))
        towns[town2].append((town1, road))
    return dijkstra(n, k, towns, 1)