class Heapnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class MaxHeap:
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
            self.maxheapify_up(node.left)
            return
        if node.right is None:
            node.right=Heapnode(data)
            self.maxheapify_up(node.right)
            return
        else:
            if self.countsize(node.left)<=self.countsize(node.right):
                self.recadd(node.left,data)
            else:
                self.recadd(node.right,data)


    def countsize(self,node):
        if node is None:
            return 0
        return 1+self.countsize(node.left)+self.countsize(node.right)

    def maxheapify_up(self,node):
        while node is not None and node!=self.root:
            parentnode=self.parentfind(node,self.root)
            if parentnode.data<node.data:
                node.data,parentnode.data=parentnode.data,node.data
                node=parentnode
            else:
                break

    def parentfind(self,node,root):
        if root.left==node or root.right==node:
            return root
        if root.left is not None:
            parent=self.parentfind(node,root.left)
            if parent is not None:return parent
        if root.right is not  None:
            parent=self.parentfind(node,root.right)
            if parent is not None:return parent

        return None

    def extract_max(self):
        if self.root is None:
            print("Heap is empty")
            return
        maxi=self.root.data
        lastnode=self.lastnfind()
        if lastnode is not None:
            self.root.data=lastnode.data
            self.heapify_down(self.root)
        else:
            self.root=None

        return maxi






    def lastnfind(self):
        queue=[self.root]
        last=None
        while len(queue)!=0:
            cur=queue.pop(0)
            last=cur
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

        if last is not None and last!=self.root :
            parent=self.parentfind(last,self.root)
            if parent is not None:
                if parent.left==last:
                    parent.left=None
                else:
                    parent.right=None

        return last

    def heapify_down(self,node):
        while node is not None:
            maxi=node
            if node.left is not None and node.left.data>maxi.data:
                maxi=node.left
            if node.right is not None and node.right.data > maxi.data:
                maxi=node.right
            if maxi!=node:
                maxi.data,node.data=node.data,maxi.data
                node=maxi
            else:
                break

























