class BSTnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BSTtree:
    def __init__(self):
        self.root=None

    def add(self,data):
        if self.root is None:
            self.root=BSTnode(data)
            return
        self.recadd(data,self.root)

    def recadd(self,data,node):
        if data<node.data:
            if node.left is None:
                node.left=BSTnode(data)
            else:
                self.recadd(data,node.left)
                
        elif data>node.data:
            if node.right is None:
                node.right=BSTnode(data)
            else:
                self.recadd(data,node.right)

    def display(self):
        result=[]
        self.recdisin(self.root,result)
        print(result)

    def recdisin(self,node,result):
        if node is None:
            return node
        else:
            self.recdisin(node.left,result)
            result.append(node.data)
            self.recdisin(node.right,result)
            
    def recdispre(self,node,result):#create separate search
        if node is None:
            return node
        else:
            result.append(node.data)
            self.recdispre(node.left,result)
            self.recdispre(node.right,result)

    def recdisinpos(self,node,result):#create separate search
        if node is None:
            return node
        else:
            self.recdisinpos(node.left,result)
            self.recdisinpos(node.right,result)
            result.append(node.data)

    def remove(self,data):
        if self.root is None:
            print("no tree")
            return
        if self.root.data==data:
            self.root=None
            return
        self.recrem(data,self.root)

    def recrem(self,data,node):
        if node is not None and node.left.data==data:
            node.left=None
            return
        elif node is not None and node.right.data==data:
            node.right=None
            return
        elif data<node.data:
            self.recrem(data,node.left)
        elif data>node.data:
            self.recrem(data,node.right)

    def search(self,data):
        nodefound=self.recsea(data,self.root)
        if nodefound is not None:
            print("true")
        else:
            print("false")

    def recsea(self,data,node):
        if node is None:
            return node
        if node is not None and node.data==data:
            return node
        elif data<node.data:
            return self.recsea(data,node.left)
        elif data>node.data:
            return self.recsea(data,node.right)
        

            
            




