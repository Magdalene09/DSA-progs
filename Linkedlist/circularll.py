class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class cll:
    def __init__(self):
        self.head=None

    def disp(self):
        if self.head is None:
            print("empty")
            return
        cur=self.head
        while cur.next!=self.head:
            print(cur.data)
            cur=cur.next
        print()

    def insend(self,data):
        newnode=Node(data)
        if self.head is None:
            newnode.next=newnode
            self.head=newnode
            return
        cur=self.head
        while cur.next!=self.head:
            cur=cur.next
        cur.next=newnode
        newnode.next=self.head

    def insbeg(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=newnode
            return
        cur=self.head
        while cur.next!=self.head:
            cur=cur.next
        cur.next=newnode
        newnode.next=self.head
        self.head=newnode

    def rem(self,data):
        if self.head is None:
            print("empty")
            return
        cur=self.head
        if cur.data==data:#remove head
            if cur.next==self.head:
                self.head=None
                return
            while cur.next!=self.head:
                cur=cur.next
                cur.next=self.head.next
                self.head=self.head.next
                return
        prev=self.head
        cur=self.head.next
        while cur!=self.head:#remove anywhere and end
            if cur.data==data:
                prev.next=cur.next
                return
            prev=cur
            cur=cur.next

        print("key not found")
