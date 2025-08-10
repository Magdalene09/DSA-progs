class Heapnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Heap:
    def __init__(self):
        self.root=None

    def add(self,data):
        if self.root is None:
            self.root=Heapnode(data)
            return

        self.recadd(self.root,data)


    def recadd(self,node,data):
        if node.left is None:
            node.left=Heapnode(data)
            self.heapify_up(node.left)
        elif node.right is None:
            node.right = Heapnode(data)
            self.heapify_up(node.right)
        else:
            if self.getcount(node.left)<=self.getcount(node.right):
                self.recadd(node.left,data)
            else:
                self.recadd(node.right,data)



    def getcount(self,node):
        if node is None:
            return 0
        return 1+self.getcount(node.left)+self.getcount(node.right)

    def heapify_up(self,node):
        while node!=self.root and node is not None:
            parentnode=self.parentnode(node,self.root)
            if parentnode.data>node.data:
                parentnode.data,node.data=node.data,parentnode.data
                node=parentnode
            else:
                break

    def parentnode(self,node,root):
        if root.left==node or root.right==node:
            return root
        if root.left is not None:
            parent=self.parentnode(node,root.left)
            if parent is not None:return parent

        if root.right is not None:
            parent=self.parentnode(node,root.right)
            if parent is not None:return parent

        return None

    def extract_min(self):
        if self.root is None:
            print("Heap is empty")
            return
        mini=self.root.data
        lastnode=self.lastnodefind()
        if lastnode is not None:
            self.root.data= lastnode.data
            self.heapify_down(self.root)
        else:
            self.root=None

        return mini



    def lastnodefind(self):
        queue=[self.root]
        last=None
        while len(queue)!=0:
            cur=queue.pop(0)
            last=cur
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)


        if last is not None and last!=self.root:
            parent=self.parentnode(last,self.root)
            if parent is not None:
                if parent.left==last:
                    parent.left=None
                else:
                    parent.right = None

        return last

    def heapify_down(self,node):
        while node is not None:
            small=node
            if node.left is not None and node.left.data<small.data:
                small=node.left
            if node.right is not None and node.right.data<small.data:
                small=node.right
            if small!=node:
                small.data,node.data=node.data,small.data
                node=small
            else:
                break























