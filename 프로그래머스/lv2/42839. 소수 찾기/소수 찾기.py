from itertools import permutations
from math import sqrt


def prime_number(n) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers) -> int:
    answer = 0
    check = set([0, 1])

    for i in range(1, len(numbers) + 1):
        for per in permutations(numbers, i):
            num = int(''.join(per))
            if num not in check:
                if prime_number(num):
                    answer += 1
                check.add(num)

    return answer