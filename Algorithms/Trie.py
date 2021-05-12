# Implement Trie

# Trie node class
class TrieNode:

    def __init__(self):
        self.children = [None] * 26 # because there are 26 alphabets (a-z)
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def __str__(self):
        cur_ndoe = self.root

    # initialize an empty node
    def getNode(self):
        return TrieNode()

    def charToIdx(self,ch): # a - z = 0 - 25
        return ord(ch) - ord('a') # ord(ch) - 97

    def insert(self,word):
        cur_node = self.root
        for letter in word:
            idx = self.charToIdx(letter)
            if cur_node.children[idx] == None:
                cur_node.children[idx] = self.getNode()
            cur_node = cur_node.children[idx]

        cur_node.isLeaf = True

    def search(self,word):
        cur_node = self.root
        for letter in word:
            idx = self.charToIdx(letter)
            if cur_node.children[idx] == None:
                return False
            cur_node = cur_node.children[idx]

        if cur_node.isLeaf ==False:
            return False
        return True

if __name__ =="__main__":

    T = Trie()

    T.insert("there")
    T.insert("the")
    T.insert("omg")
    T.insert("hey")

    print("{} --- {}",'there', T.search('there'))
    print("{} --- {}",'ahahaha', T.search('ahahaha'))
    print("{} --- {}",'omg', T.search('omg'))
    print("{} --- {}",'hey', T.search('hey'))
    print("{} --- {}",'heyy', T.search('heyy'))