from collections import Counter


def solution(weights: list) -> int:
    answer, counter = 0, Counter(weights)

    for i in counter:
        answer += counter[i] * (counter[i] - 1) // 2
        answer += counter[i] * counter[i * 3 / 2]
        answer += counter[i] * counter[i * 2]
        answer += counter[i] * counter[i * 4 / 3]

    return answer