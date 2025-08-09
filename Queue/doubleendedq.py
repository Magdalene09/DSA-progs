'''
from collections import deque
class newone:#import module using deque
    def __init__(self,mlen):
        self.dq=deque(maxlen=mlen)

    def inf(self,value):
        self.dq.appendleft(value)

    def inr(self,value):
        self.dq.append(value)

    def remf(self):
        self.dq.popleft()

    def remr(self):
        self.dq.pop()

    def isempty(self):
        if len(self.dq)==0:
            return True
        else:
            return False
    def front(self):
        return self.dq[0]
    
    def rear(self):
        return self.dq[-1]
    
    def val(self,index):
        return self.dq[index]
'''

class dque:#manual implementation
    def __init__(self,cap):
        self.cap=cap
        self.size=0
        self.front=0
        self.rear=-1
        self.q=[None]*cap

    def isfull(self):
        return self.size==self.cap

    def isemp(self):
        return self.size==0

    def insr(self,value):
        if self.isfull():
            print("value cannot be entered")
            return
        self.rear+=1
        self.q[self.rear]=value
        self.size+=1

    def insf(self,value):
        if self.isfull():
            print("value cannot be entered")
            return
        if self.front>0:
            self.front-=1
            self.q[self.front]=value
        else:
            if self.rear+1>=self.cap:
                print("cannot shift")
                return
            for i in range(self.rear,self.front-1,-1):
                self.q[i+1]=self.q[i]
            self.q[self.front]=value
            self.rear+=1
        self.size+=1

    def delf(self):
        if self.isemp():
            print("no element in queue")
            return
        self.q[self.front]=None
        self.front+=1
        self.size-=1

    def delr(self):
        if self.isemp():
            print("no element in queue")
            return
        self.q[self.rear]=None
        self.rear-=1
        self.size-=1





        
    





























        
