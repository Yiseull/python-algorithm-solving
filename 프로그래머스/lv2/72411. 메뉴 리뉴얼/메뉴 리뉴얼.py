from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for course_size in course:
        com = []
        for order in orders:
            com += combinations(sorted(order), course_size)
        counter = Counter(com).most_common()
        answer += [''.join(key) for key, value in counter if value == counter[0][1] > 1]
        
    return sorted(answer)