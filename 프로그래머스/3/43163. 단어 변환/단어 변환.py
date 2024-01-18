from collections import deque


def check(word1, word2) -> bool:
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return True if count < 2 else False


def solution(begin: str, target: str, words: list) -> int:
    q = deque([begin])
    visited = dict()
    visited[begin] = 0
    for word in words:
        visited[word] = -1
    while q:
        v = q.popleft()
        for word in words:
            if visited[word] == -1 and check(v, word):
                visited[word] = visited[v] + 1
                if target == word:
                    return visited[word]
                q.append(word)
                
    return 0