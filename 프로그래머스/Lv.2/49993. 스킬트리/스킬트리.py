INIT = -1
IMPOSSIBLE = -2


def solution(skill: str, skill_trees: list) -> int:
    answer = 0
    for user_skill in skill_trees:
        status = INIT
        for i, sk in enumerate(user_skill):
            for j, sk2 in enumerate(skill):
                if sk == sk2:
                    if status > j or (j - status > 1):
                        status = IMPOSSIBLE
                        break
                    status = j
            
            if status == IMPOSSIBLE or status == len(skill) - 1:
                break
        if status != IMPOSSIBLE:
            answer += 1
        
    return answer
                