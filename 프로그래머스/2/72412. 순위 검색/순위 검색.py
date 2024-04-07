from bisect import bisect_left
from collections import defaultdict


def solution(infos: list, queries: list) -> list:
    info_dict = defaultdict(list)
    for info in infos:
        language, job, career, food, score = info.split()
        for l in ('-', language):
            for j in ('-', job):
                for c in ('-', career):
                    for f in ('-', food):
                        info_dict[(l, j, c, f)].append(int(score))
    
    for key in info_dict.keys():
        info_dict[key].sort()
    
    answer = []
    for query in queries:
        language, job, career, food_score = query.split(' and ')
        food, score = food_score.split()
        left = bisect_left(info_dict[(language, job, career, food)], int(score))
        answer.append(len(info_dict[(language, job, career, food)]) - left)
    return answer