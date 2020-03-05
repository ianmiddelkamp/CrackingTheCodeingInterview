class Node:
     next = None
     data = None
     def __init__(self, d):
          self.data = d

class EmptyStackException(Exception):
     pass

class Stack:
     top = None

     def __init__(self):
          pass

     def pop(self):
          if self.top == None:
              raise EmptyStackException("Empty Stack")
          data = self.top.data
          top = self.top.next
          return data

     def push(self,data):
          node = Node(data)
          node.next =self.top 
          self.top = node

     def peek(self):
          if self.top == None:
               raise EmptyStackException("Empty Stack")
          return top.data

     def isEmpty(self):
          return self.top == None

     