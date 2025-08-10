class Dsa:
    def __init__(self,isdirected=False):
        self.graph={}
        self.isdirected=isdirected

    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
        else:
            print("vertex already exists")

    def addedge(self,vertex1,vertex2):
        self.addvertex(vertex1)
        self.addvertex(vertex2)
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if not self.isdirected:
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)


    def display(self):
        for key,value in self.graph.items():
            print(f'{key} => {value}')

    def disvert(self):
        for key in self.graph:
            print(key)

    def disedge(self):
        for key,value in self.graph.items():
            for i in value:
                print(f'({key},{i})')

    def removevert(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key,value in self.graph.items():
                if vertex in value:
                    value.remove(vertex)
        else:
            print("value doesnt exist")

    def isedge(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if self.isdirected:
                return vertex2 in self.graph[vertex1]
            else:
                return vertex2 in self.graph[vertex1] or vertex1 in self.graph[vertex2]
        return False



    def removeedge(self,vertex1,vertex2):
        if self.isedge(vertex1,vertex2):
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if not self.isdirected:#same as if isdirected ==False
                if vertex1 in self.graph[vertex2]:
                    self.graph[vertex2].remove(vertex1)
        else:
            print("the vertex1 or 2 doesnt have edges")

    def dfs(self,start,visited=None):#set does not allow duplicated but similar to list
        if visited is None:
            visited=set()
        if start not in visited:
            visited.add(start)
            print(start,end=" ")
            for child in self.graph[start]:
                self.dfs(child,visited)

    def bfs(self,start):
        visited={start}
        queue=[start]
        while len(queue)>0:
            current=queue.pop(0)
            print(current,end=" ")
            for child in self.graph[current]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)

    def shortpath(self,start,stop):
        visited={start}
        queue=[(start,[start])]
        while len(queue)>0:
            current,path=queue.pop(0)
            for child in self.graph[current]:
                if child == stop:
                    return path+[child]
                if child not in visited:
                    visited.add(child)
                    queue.append((child,path+[child]))
        return None





