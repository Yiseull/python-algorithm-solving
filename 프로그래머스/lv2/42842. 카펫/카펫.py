def solution(brown, yellow):
    area = brown + yellow
    for i in range(2, area):
        if area % i == 0:
            a, b = i, area // i
            if 2 * (a + b) - 4 == brown:
                return [b, a]