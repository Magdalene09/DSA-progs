class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None

    def addend(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        cur=self.head
        while cur.next is not none:
            cur=cur.next

        cur.next=newnode
        newnode.prev=cur

    def addst(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        self.head.prev=newnode
        newnode.next=self.head
        self.head=newnode

    def display(self):
        cur=self.head
        while cur is not None:
            print(cur.data,end=" ")
            cur=cur.next
        print()

    def rem(self,data):
        if self.head is None:
            print("no linked list bro")
        if self.head.data==data:
            self.head=self.head.next
            if self.head is not None:
                self.head.prev=None
                return
        cur=self.head
        while cur is not None and cur.data!=data:
            cur=cur.next
        if cur is None:
            print("data not found bro")
        if cur.prev is not None:
            cur.prev.next=cur.next
        if cur.next is not None:
            cur.next.prev=cur.prev
        
        
            
                
            
        

    
            
