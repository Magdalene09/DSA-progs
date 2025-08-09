class tnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class bintree:
    def __init__(self):
        self.root=None

    def add(self,data):
        if self.root is None:
            self.root=tnode(data)
            return
        self.recursiveadd(data,self.root)

    def recursiveadd(self,data,node):
        if node.left is None:
            node.left=tnode(data)
        elif node.right is None:
            node.right=tnode(data)
        else:
            self.recursiveadd(data,node.left)#will put everything in left side and node.right will put in right side
    def display(self,depth=0,node=None):
        if node is None:
            node=self.root
        print(' '*depth,node.data)
        if node.left is not None:
            self.display(depth+1,node.left)
        if node.right is not None:
            self.display(depth+1,node.right)

    def remove(self,data):
        if self.root is None:
            print("no tree")
            return
        if self.root.data==data:
            self.root=None
            return
        self.recursiverem(data,self.root)
    

    def recursiverem(self,data,node):
        if node.left is None or node.left.data==data:
            node.left=None
            return
        if node.right is None or node.right.data==data:
            node.right=None
            return
        if node.left is not None:
            self.recursiverem(data,node.left)
        if node.right is not None:
            self.recursiverem(data,node.right)

    def search(self,data):
        nodefound=self.recursivesea(data,self.root)
        if nodefound is not None:
            print("True")
        else:
            print("False")
    def recursivesea(self,data,node):
        if node is None or node.data==data:
            return node
        return self.recursivesea(data,node.left) or self.recursivesea(data,node.right)
        
