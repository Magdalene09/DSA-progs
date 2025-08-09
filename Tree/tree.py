class Tnode:
    def __init__(self,data):
        self.data=data
        self.child=[]

class Tree:
    def __init__(self):
        self.root=None

    def add(self,data,pardata=None):
        node=Tnode(data)
        if self.root is None:
            self.root=node
            return

        parentnode=self.findnode(pardata,self.root)#finding parent node without data
        if parentnode is not None:
            parentnode.child.append(node)

    def findnode(self,data,node):
        if node.data==data:
            return node

        for c in node.child:
            nodefound=self.findnode(data,c)
            if nodefound is not None:
                return nodefound
        return None
    def display(self,depth=0,node=None):
        if node is None:
            node=self.root
        if node is None:
            print("empty")
            return
        print(' '*depth,node.data)
        for c in node.child:
            self.display(depth+1,c)

    def remove(self,data):
        if self.root is None:
            print("tree is empty bro")
            return
        if self.root.data==data:
            self.root=None
            return
        parentnode=self.findpn(data,self.root)
        if parentnode is not None:
            for c in parentnode.child:
                if c.data==data:
                    parentnode.child.remove(c)
                    return
        print("node not found")


    def findpn(self,data,node):#finding parentnode with data
        for c in node.child:
            if c.data==data:
                return node
            nodefound=self.findpn(data,c)
            if nodefound is not None:
                return nodefound
        return None

    def dfstraversal(self,node):
        if node is not None:
            print(node.data,end=" ")
            for c in node.child:
                self.dfstraversal(c)


    def iterative_dfs(root):
    if root is None:
        return

    stack = [root]  # start with the root node

    while stack:
        node = stack.pop()  # take the top node
        print(node.data, end=" ")

        # Add children in reverse order so left child is processed first
        for child in reversed(node.child):
            stack.append(child)
            

    def bfstraversal(self,node):
        if node is None:
            return
        queue=[node]
        while queue:#same as while len of queue greator or not equal to zero all same
            cur=queue.pop(0)
            print(cur.data,end=" ")
            for c in cur.child:
                queue.append(c)
            
