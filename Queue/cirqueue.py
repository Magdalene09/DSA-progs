'''
class cirque:#normal implementation
    def __init__(self,k):
        self.front=0
        self.rear=0
        self.size=0
        self.k=k
        self.q=[None]*k

    def isfull(self):
        if self.size==self.k:return True
        return False
    def isempty(self):
        if self.size==0:return True
        return False
    def enq(self,value):
        if self.isfull():return False
        self.q[self.rear]=value
        self.size+=1
        self.rear=(self.rear+1)%self.k
    def deq(self):
        if self.isempty():return False
        self.front=(self.front+1)%self.k
        self.size-=1

    def fr(self):
        return self.q[self.front]
    def rr(self):
        return self.q[self.rear-1]
'''

from collections import deque
class cq:#deque module implementation
    def __init__(self,val):
        self.ccq=deque(maxlen=val)

    def enq(self,num):
        self.ccq.append(num)

    def deq(self):
        self.ccq.popleft()

    def front(self):
        return self.ccq[0]

    def rear(self):
        return self.ccq[-1]

    def isempty(self):
        if len(self.ccq)==0:
            return True
        return False


































        
