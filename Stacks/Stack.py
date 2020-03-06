class Node:
     next = None
     data = None
     def __init__(self, d):
          self.data = d

class EmptyStackException(Exception):
     pass


#LIFO. node.next is oriented towards the bottom of the stack.
class Stack:
     top = None

     def __init__(self):
          pass

     def generateFromArray(self, arr):        
          for i in range(len(arr)):
               el = arr[i]
               self.push(el)

     def returnAsArray(self):
          node = self.top
          arr = []
          while node != None:
               arr.append(node.data)
               node = node.next
          return arr

     def pop(self):
          if self.top == None:
              raise EmptyStackException("Empty Stack")
          data = self.top.data
          self.top = self.top.next
          return data

     def push(self,data):
          node = Node(data)
          node.next =self.top 
          self.top = node

     def peek(self):
          if self.top == None:
               raise EmptyStackException("Empty Stack")
          return self.top.data

     def isEmpty(self):
          return self.top == None

#FIFO node.next is oriented towards the end of the queue.
class Queue:

     first = None
     last = None

     def __init__(self):
          pass

     def add(self, data):
          node = Node(data)
          if self.last != None:
               self.last.next = node   
          self.last = node
          if self.first == None:
               self.first = self.last

     def remove(self):
          if self.first == None:
               raise EmptyStackException("Empty Stack")
          data = self.first.data
          self.first = self.first.next
          if self.first == None:
               self.last = None
          return data

     def peek(self):
          if self.first == None:
               raise EmptyStackException("Empty Stack")
          return self.first.data
     
     def isEmpty(self):
          return self.first == None




     