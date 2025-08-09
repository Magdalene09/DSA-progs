
class Node:#only one occurrence is removed
    def __init__(self,data):
        self.data=data
        self.pointer=None

class ll:
    def __init__(self):
        self.head=None

    def add(self,value):#insertion at the end
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
        else:
            cur=self.head
            while cur.pointer is not None:
                cur=cur.pointer
            cur.pointer=newnode

    def addp(self,pos,value):
        newnode=Node(value)
        if pos==0:
            newnode.pointer=self.head
            self.head=newnode
            return
        cur=self.head
        count=0
        while cur is not None and count<pos-1:
            cur=cur.pointer
            count+=1
        if cur is None:
            print("went outside")
            return
        newnode.pointer=cur.pointer
        cur.pointer=newnode
        
        
    def disp(self):
        cur=self.head
        while cur is not None:
            print(cur.data,end=" ")
            cur=cur.pointer
        print()

    def remove(self,value):#removing at all places
        if self.head is not None:
            if self.head.data==value:
                self.head=self.head.pointer
            else:
                cur=self.head
                while(cur.pointer is not None and cur.pointer.data!=value):
                    cur=cur.pointer
                if cur.pointer is not None:
                    cur.pointer=cur.pointer.pointer
                else:
                    print("No elements in linked list")

    def newrem(self,value):#removing for all occurences of same value
        while self.head is not None and self.head.data==value:
            self.head=self.head.pointer

        cur=self.head
        while cur is not None and cur.pointer is not None:
            if cur.pointer.data==value:
                cur.pointer=cur.pointer.pointer
            else:
                cur=cur.pointer


        
            
            
            
        
