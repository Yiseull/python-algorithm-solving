'''
- 체육수업을 들을 수 있는 학생의 최댓값 = 체육복이 1개 있는 학생 수 + 체육복을 도난당했지만 빌린 학생 수
- 여벌 체육복이 있는 학생도 도난당했을 수 있음 => 체육복 1개 있는 학생으로 계산
- 여벌 체육복이 있는 학생은 자신의 앞번호나 뒷번호 학생에게만 빌려줄 수 있음 -> 앞번호부터(그리디)
'''
def solution(n: int, lost: list, reserve: list) -> int:
    lost, reserve = set(lost), set(reserve)
    lost, reserve = lost - reserve, reserve - lost
    answer = n - len(lost)
    for r in reserve:
        for l in lost:
            if -2 < r - l < 2:
                answer += 1
                lost.remove(l)
                break

    return answer