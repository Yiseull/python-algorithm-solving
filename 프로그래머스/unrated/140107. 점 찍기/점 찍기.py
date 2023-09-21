from math import sqrt


def solution(k, d):
    answer = 0
    dd = d ** 2
    for x in range(0, d + 1, k):
        yy = dd - x ** 2
        answer += sqrt(yy) // k + 1
    return answer