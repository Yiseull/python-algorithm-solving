'''
1. report를 순회하면서 신고자들을 신고한 이용자들을 딕셔너리로 만든다. -> O(m) = O(200,000)
2. 신고자들의 신고 횟수가 k 이상이면 신고한 이용자들의 answer 배열의 값을 +1 한다. -> O(n^2) -> O(1,000,000)
'''
def solution(id_list: list, report: list, k: int) -> list:
    answer = {id : 0 for id in id_list}
    report_dict = dict()
    for r in report:
        user, reported = r.split()
        if reported not in report_dict:
            report_dict[reported] = set()
        report_dict[reported].add(user)
        
    for values in report_dict.values():
        if len(values) < k:
            continue
        for user in values:
            answer[user] += 1
    
    return list(answer.values())