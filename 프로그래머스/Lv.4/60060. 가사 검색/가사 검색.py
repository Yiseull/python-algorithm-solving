from collections import defaultdict

class Node(object):
    def __init__(self, key):
        self.key = key
        self.remain_length = defaultdict(int)
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        curr_node.remain_length[len(string)] += 1

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            curr_node.remain_length[len(string)] += 1

    def starts_with(self, prefix, length):
        curr_node = self.head

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0

        return curr_node.remain_length[length]


def solution(words, queries):
    trie = Trie()
    reverse_trie = Trie()

    for word in words:
        trie.insert(word)
        reverse_trie.insert(word[::-1])

    answer = []

    for query in queries:
        if query[0] == '?':
            res = reverse_trie.starts_with(query[::-1].replace('?', ''), len(query))
        else:
            res = trie.starts_with(query.replace('?', ''), len(query))
        answer.append(res)

    return answer
