from collections import defaultdict
import sys
class TrieNode:

    def __init__(self):
        self.children = {}
        self.childrenCnt = defaultdict(int)      # length : cnt

class Trie:
    def __init__(self):
        self.root = self.getNode()

    # initialize an empty node
    def getNode(self):
        return TrieNode()

    def insert(self,word):
        cur_node = self.root
        n = len(word)
        for letter in word:
            if letter not in cur_node.children:
                cur_node.children[letter] = self.getNode()
            cur_node.childrenCnt[str(n)] += 1
            cur_node = cur_node.children[letter]

    def search(self,word):
        cur_node = self.root            # reach the end of prefix
        n = len(word)
        for letter in word:
            if letter == '?' :break

            if letter not in cur_node.children:
                return 0
            cur_node = cur_node.children[letter]

        return cur_node.childrenCnt[str(n)]



def solution(words, queries):
    T,invertedT = Trie(), Trie()
    answer=[]

    for w in words:
        T.insert(w)
        invertedT.insert(w[::-1])

    for q in queries:
        ans=0
        if q[0] =='?' and q[-1]=='?':
            ans = T.root.childrenCnt[str(len(q))]
        elif q[0] != '?':
            ans = T.search(q)
        else:
            ans = invertedT.search(q[::-1])
        answer.append(ans)

    return answer


if __name__ =='__main__':
    input = sys.stdin.readline

    words = list(map(str,input().split()))
    queries = list(map(str,input().split()))

    ans = solution(words,queries)
    print(ans)
#
# frodo front frost frozen frame kakao
# fro?? ????o fr??? fro??? pro?