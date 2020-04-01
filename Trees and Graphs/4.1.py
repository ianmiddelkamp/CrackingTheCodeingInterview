#!/usr/bin/python
# -*- coding: utf-8 -*-
QUESTION = "4.1"
from Graph import NodeState, Graph, Node
from Stack import Queue
import time
import sys



def breadthfirstsearch(graph, start, end):
     if start == end:
          return True
     queue = Queue()
     nodes = graph.getNodes()     
     queue.add(nodes[0])
     
     while (queue.isEmpty() == False):
          node = queue.remove()
          children = node.getChildren()
          if children!=None:
               for i in range(0, len(children)):
                    child = children[i]
                    if child.isVisited() == False:
                         if child == end: 
                              return True
                         else:
                              queue.add(child)
                         
         
          node.setVisited()             
     return False


if __name__ == '__main__':
     start = time.perf_counter()
     b = Node("b", None)
     c = Node("c", None)
     d = Node("d", None)
     e = Node("e", None)
     f = Node("f", None)
     g = Node("g", None)
     h = Node("h", None)
     i = Node("i", None)
     j = Node("j", None)
     k = Node("k", None)
     test = {
          "l":[b, c, d],
          "m":[f, g, h],
          "n":[f, i, j],
          "o":[k, g, c]
     }

     print("Test for equality")
     print(test["m"][0] == test["n"][0])
     print(test["m"][0] == test["n"][1])
     print("Test for inequality")
     print(test["m"][0] != test["n"][0])
     print(test["m"][0] != test["n"][1])
     graph = Graph()
     graph.createFromAdjacencyList(test)
     graph.printGraph()
     end = time.perf_counter()
     print(breadthfirstsearch(graph, test["m"][0], test["n"][0]))

     print('Total Time:\n' + str(end - start))
