from enum import Enum

class NodeState(Enum):
     VISITED = 1     
     UNVISITED = 0

class Graph:
     nodes = []

     def __init__(self):
          pass
     def addNode(self, node):
         self.nodes.append(node)
     def getNodes(self):
          return self.nodes

     def createFromAdjacencyList(self,alist):
       
          for Name in alist:
             
               children = alist[Name]
               
               node = Node(Name, children)
               self.addNode(node)

     def toAdjacencyList(self):
          adjacencylist = {}
          for i in range(0, len(self.nodes)):
               node = self.nodes[i]
               name = node.getName()
               children = node.getChildren()
               childlist = []
               if children != None and len(children)> 0: 
                    for i in range(0, len(children)):
                         childlist.append(children[i])
               adjacencylist[name] = children
          return adjacencylist

     def printGraph(self):
     
          for i in range(0, len(self.nodes)):

               node = self.nodes[i]
               name = node.getName()
               children = node.getChildren()
               print("Node:")
               print(name)
               if children != None and len(children)> 0: 
                    string = ""
                    for i in range(0, len(children)):
                         string += children[i].getName()
                    print("Children:" + string)
        
          
        

class Node:
     name = None
     children = []
     state = NodeState.UNVISITED
     def __init__(self, Name, Children):
          self.name = Name
          self.children = Children

     def getChildren(self):
          return self.children
     
     def getName(self):
          return self.name

     def getState(self):
          return self.state
     def setVisited(self):
          self.state = NodeState.VISITED
     def isVisited(self):
          return self.state == NodeState.VISITED


