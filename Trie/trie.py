class TrieN:
    def __init__(self):
        self.child={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieN()

    def add(self,word):
        cur=self.root
        for letter in word:
            if letter not in cur.child:
                cur.child[letter]=TrieN()
            cur=cur.child[letter]
        cur.end=True

    def search(self,word):
        cur=self.root
        for letter in word:
            if letter not in cur.child:
                return False
            cur=cur.child[letter]
        return cur.end#if cur.end is true will give true or false then false

    def remove(self,word):
        if not self.search(word):
            print("No word bro")
            return
        cur=self.root
        stack=[]
        for letter in word:
            stack.append((cur,letter))
            cur=cur.child[letter]
        cur.end=False#word is not there but the letters still exist

        for parent,letter in reversed(stack):#removing letters if they do not have any children or not an end of word
            node=parent.child[letter]
            if not node.child and not node.end:
                del parent.child[letter]
            else:
                break
        print("word removed")

    def startswith(self,prefix):#checking
        cur=self.root
        for letter in prefix:
            if letter not in cur.child:
                return False
            cur=cur.child[letter]
        return True

    def starting(self,prefix):
        words=[]
        cur=self.root
        for letter in prefix:
            if letter not in cur.child:
                return words
            cur=cur.child[letter]

        def dfs(node,path):
            if node.end:#if node.end ==TRUE
                words.append(''.join(path))
            for parent,childn in node.child.items():
                dfs(childn,path+[parent])

        dfs(cur,list(prefix))
        return words#return sorted(words) gives in sorted order

    def display(self):
        words=[]

        def dfs(node,path):
            if node.end:
                words.append(''.join(path))
            for parent,childn in node.child.items():
                dfs(childn,path+[parent])

        dfs(self.root,[])
        return words





















