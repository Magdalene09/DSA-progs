'''
class stack:#using class or it can be implemented normally (list)
    def __init__(self):
        self.st=[]

    def push(self,value):
        self.st.append(value)

    def pop(self):
        if self.isempty():
            return "no element in stack"
        return self.st.pop()
    def top(self):
        if self.isempty():
            return "no element in stack"
        return self.st[-1]
    def isempty(self):
        return len(self.st)==0

    def search(self,item):
        if item in self.st:
            pos=len(self.st)-self.st[::-1].index(item)
            return pos
        else:
            return "item not in stack"
  '''
class newst:
    def __init__(self,cap):
        self.cap=cap
        self.top=-1
        self.stk=[None]*cap
        self.size=0

    def isfull(self):
        return self.size==self.cap
            
    def isemp(self):
        return self.size==0
    def ins(self,value):
        if self.isfull():
            print("value cannot be inserted")
            return
        self.top+=1
        self.stk[self.top]=value
        self.size+=1

    def dele(self):
        if self.isemp():
            print("value cannot be deleted")
            return
        self.stk[self.top]=None
        self.top-=1
        self.size-=1
    def peek(self):
        if self.isemp():
            return "empty"
        return self.stk[self.top]
