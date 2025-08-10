class Hashmap:
    def __init__(self,cap):
        self.cap=cap
        self.hashlist=[None]*self.cap

    def getindex(self,key):
        return hash(key)%self.cap

    def add(self,key,value):#if I use set item function then directly key value entered like dictionary
        index=self.getindex(key)
        if self.hashlist[index] is None:
            self.hashlist[index]=[[key,value]]
        else:
            sublist=self.hashlist[index]#update old to new
            for pairs in sublist:
                if pairs[0]==key:
                    pairs[1]=value
                    return
            self.hashlist[index].append([key, value])

    def get(self,key):
        index = self.getindex(key)
        if self.hashlist[index] is not None:
            sublist=self.hashlist[index]
            for pairs in sublist:
                if pairs[0]==key:
                    return pairs[1]
        return "key not found"

    def dele(self,key):
        index=self.getindex(key)
        if self.hashlist[index] is not None:
            sublist=self.hashlist[index]
            for i,pairs in enumerate(sublist):
                if pairs[0]==key:
                    del self.hashlist[index][i]
                    return
        return "key not found"

    def display(self):
        for i,pairs in enumerate(self.hashlist):
            print(f"{i}:{pairs}")








