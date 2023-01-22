class graph:
    def __init__(self,edges):
        self.edges=edges
        self.dict={}

        for start,end in self.edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start]=[end]
        print("graph=",self.dict)

    def get_path(self,start,end,path=[]):
        path=path+[start]

        if start==end:
            return [path] 

        if start not in self.dict:
            return []

        path=[]
        
        for node in self.dict[start]:
            if node not in path:
                new_path=self.get_path(node,end,path)
                for p in new_path:
                    path.append(p)
        return path

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.dict:
            return None

        shortest_path = None
        for node in self.dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__=='__main__':
    routes=[
        {"mumbai",'paris'},
        {'mumbai','dubai'},
        {'paris','dubai'},
        {'paris','new yok'},
        {'dubai','new york'},
        {'new york','toronto'},
    ]

    r_graph=graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",r_graph.get_path(start,end))
    print(f"Shortest path between {start} and {end}: ", r_graph.get_shortest_path(start,end))

    start = "Dubai"
    end = "new york"

    print(f"All paths between: {start} and {end}: ",r_graph.get_path(start,end))
    print(f"Shortest path between {start} and {end}: ", r_graph.get_shortest_path(start,end))

    # d={
    #     'mumbai':['pris','dubai']
    # }