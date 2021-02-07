from collections import defaultdict
import sys

class node():
    def __init__(self):
        self.children = {}
        self.cnt = 0

class Trie():

    def __init__(self):
        self.root = node()

    def insert(self,word):
        current_node = self.root

        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = node()
            current_node.cnt += 1
            current_node = current_node.children[letter]

    def search(self,word):
        current_node = self.root
        for letter in word:
            if letter == '?' :break
            elif letter not in current_node.children:
                return 0
            current_node = current_node.children[letter]


        return current_node.cnt

def solution(words, queries):
    T, invertedT = defaultdict(Trie), defaultdict(Trie)

    answer=[]
    for w in words:
        n = len(w)
        T[n].insert(w)
        invertedT[n].insert(w[::-1])

    for q in queries:
        n = len(q)
        ans = 0
        if q[-1] =='?':
            ans = T[n].search(q)
        else:
            ans = invertedT[n].search(q[::-1])
        answer.append(ans)


    return answer


input = sys.stdin.readline

w = list(map(str,input().split()))
q = list(map(str, input().split()))

print(solution(w,q))

# frodo front frost frozen frame kakao
# fro?? ????o fr??? fro??? pro?



