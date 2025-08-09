'''
class queue:#implementation using list
    def __init__(self):
        self.q=[]

    def enqueue(self,value):
        self.q.append(value)

    def dequeue(self):
        self.q.pop(0)

    def isempty(self):
        if len(self.q)==0:
            return True
        else:
            return False

    def front(self):
        return self.q[0]


'''


'''
from queue import Queue
class Qu:#import method of using queue
    def __init__(self,maxi):
        self.var=Queue(maxsize=maxi)

    def insert(self,value):
        self.var.put(value)

    def delt(self):
        self.var.get()

    def isempty(self):#for full we can use .full() to find whether the queue is full or not
        if self.var.empty():
            return True
        else:
            return False
    def fro(self):
        return self.var.queue[0]
        '''

class newq:#manual implementation
    def __init__(self,cap):
        self.cap=cap
        self.size=0
        self.front=0
        self.rear=-1
        self.qu=[None]*cap

    def isfull(self):
        return self.cap==self.size
    def isemp(self):
        return self.size==0
    def ins(self,value):
        if self.rear+1>=self.cap:
            print('NO SPACE')
            return
        self.rear+=1
        self.qu[self.rear]=value
        self.size+=1
    def dele(self):
        if self.isemp():
            print("empty")
            return
        self.qu[self.front]=None
        self.front+=1
        self.size-=1
    def fro(self):
        return self.qu[self.front]




        
