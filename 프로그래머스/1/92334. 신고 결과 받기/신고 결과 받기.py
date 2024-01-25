'''
1. report를 순회하면서 신고자들을 신고한 이용자들을 딕셔너리로 만든다. -> O(m) = O(200,000)
2. 신고자들의 신고 횟수가 k 이상이면 신고한 이용자들의 answer 배열의 값을 +1 한다. -> O(n^2) -> O(1,000,000)
'''
def solution(id_list: list, report: list, k: int) -> list:
    answer, report_dict = dict(), dict()
    for id in id_list:
        answer[id], report_dict[id] = 0, set()
    
    for r in set(report):
        user, reported = r.split()
        report_dict[reported].add(user)
        
    for values in report_dict.values():
        if len(values) >= k:
            for user in values:
                answer[user] += 1
    
    return list(answer.values())