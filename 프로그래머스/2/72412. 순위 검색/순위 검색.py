from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}
    for lang in ('cpp', 'java', 'python', '-'):
        for job in ('backend', 'frontend', '-'):
            for career in ('junior', 'senior', '-'):
                for food in ('chicken', 'pizza', '-'):
                    info_dict[(lang, job, career, food)] = []
                    
    for i in info:
        data = i.split()
        for lang in (data[0], '-'):
            for job in (data[1], '-'):
                for career in (data[2], '-'):
                    for food in (data[3], '-'):
                        info_dict[(lang, job, career, food)].append(int(data[4]))
                        
    for key in info_dict.keys():
        info_dict[key].sort()
    
    for q in query:
        lang, job, career, food = q.split(' and ')
        food, score = food.split()
        answer.append(len(info_dict[(lang, job, career, food)]) - bisect_left(info_dict[(lang, job, career, food)], int(score)))
    
    return answer