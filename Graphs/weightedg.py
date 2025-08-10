class Wgraph:
    def __init__(self,isdirected=False):
        self.graph={}
        self.isdirected=isdirected

    def addvert(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]={}
        else:
            print("vertex already exists")

    def addedge(self,fromvert,tovert,weight):
        self.addvert(fromvert)
        self.addvert(tovert)
        if tovert not in self.graph[fromvert]:
            self.graph[fromvert][tovert]=weight
        else:
            print("already there")
        if not self.isdirected:
            if fromvert not in self.graph[tovert]:
                self.graph[tovert][fromvert]=weight
            else:
                print("already there")

    def removeedge(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                del self.graph[vertex1][vertex2]
            if not self.isdirected:
                if vertex1 in self.graph[vertex2]:
                    del self.graph[vertex2][vertex1]
        else:
            print("either one or both vertex doesnt exist")

    def removevert(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for i in self.graph:
                if vertex in self.graph[i]:
                    del self.graph[i][vertex]
        else:
            print("vertex doesnt exist")

    def display(self):
        for key,value in self.graph.items():
            print(f'{key}=>{value}')

    def searchvertex(self,vertex):
        return vertex in self.graph

    def searchedge(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                return True
            else:
                return False

        else:
            print("either both or one edge doesnt exist")
            return False



