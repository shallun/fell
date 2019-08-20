class graph():
        def __init__(self,vertices):
                self.graph=[[0 for column in range(vertices)]\
                             for row in range(vertices)]
                self.V=vertices
        def isSafe(self,v,pos,path):
                if self.graph[path[pos-1]][v]==0:
                              return False

                for vertex in path:
                              if vertex==v:
                                      return False
                return True
        def hamcycleUtil(self,path,pos):
            if pos==self.V:
                if self.graph[path[pos-1]][path[0]]==1:
                     return True
                else:
                     return False
            for v in range(1,self.V):
                    if self.isSafe(v,pos,path)==True:
                            path[pos]=v
                            if self.hamcycleUtil(path,pos+1)==True:
                                    return True
                            path[pos]=-1
            return False
        def hamcycle (self):
                path=[-1]*self.V
                path[0]=0
                if self.hamcycleUtil(path,1)==False:
                        print("solution does not exist \n")
                        return False
                self.printsolution(path)
                return True
                        
        def printsolution(self,path):
                              print("solution exists:following is one hamiltonian cycle")
                              for vertex in path:
                                      print(vertex)
                              print(path[0],"\n")


g1=graph(5)
g1.graph=[[0,1,0,1,0],[1,0,1,1,1],[0,1,0,0,1],[1,1,0,0,1],[0,1,1,1,0]]
g1.hamcycle()
g2=graph(5)
g2.graph=[[0,1,0,1,0],[1,0,1,1,1],[0,1,0,0,1],[1,1,0,0,0],[0,1,1,0,0]]
g2.hamcycle()
                              
                              
