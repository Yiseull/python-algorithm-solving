from collections import deque


def solution(bridge_length, weight, truck_weights) -> int:
    time = 0
    q = deque()
    total_weight = 0
    i = 0

    while 1:
        if len(q) < bridge_length:
            if i < len(truck_weights) and total_weight + truck_weights[i] <= weight:
                q.append(truck_weights[i])
                total_weight += truck_weights[i]
                i += 1
            else:
                q.append(0)
            time += 1
        else:
            total_weight -= q.popleft()

        if i == len(truck_weights) and total_weight == 0:
            break

    return time + 1