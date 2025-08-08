'''#Array implementation using array module
import array as a
arr=a.array('i',[])
n=int(input("enter the number of elements to be entered"))
for i in range(n):
    m=int(input("enter num"))
    arr.append(m)
print(arr)

key=int(input("enter the index"))
value=int(input("enter value"))
arr.insert(key,value)
print(arr)

rem=int(input("enter the index to be popped"))
arr.pop(rem)
print(arr)

new=int(input("enter the num to be searched"))
for i in range(len(arr)):
    if arr[i]==new:
        print(i,arr[i])
        break
'''
#Manual implementation
class array:
    def __init__(self,cap):
        self.cap=cap
        self.size=0
        self.arr=[None]*cap

    def isfull(self):
        return self.size==self.cap

    def isemp(self):
        return self.size==0
        
    def add(self,data,pos):
        if self.isfull():
            print("array is full")
            return
        if pos<0 or pos>self.size:
            print("not possi")
            return
        for i in range(self.size,pos,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[pos]=data
        self.size+=1

    def dele(self,pos):
        if self.isemp():
            print("deletion not possible")
            return
        if pos<0 or pos>=self.size:
            print("not possi")
            return
        for i in range(pos,self.size-1):
            self.arr[i]=self.arr[i+1]
        self.arr[self.size-1]=None
        self.size-=1

    def display(self):
        for i in range(self.size):
            print(self.arr[i])
                

        
        


