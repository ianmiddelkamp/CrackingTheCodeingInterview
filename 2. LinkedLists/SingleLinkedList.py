class Node:
     next = None
     data = None
     def __init__(self, d):
          self.data = d
          

     def appendToTail(self, d):
          end = Node(d)
          n = self
          while n.next != None:
               n = n.next
          n.next = end

     
class Index:
     value = None
     def __init__(self):
          self.value = 0
     



class SingleLinkedList:
     head = None
     def __init__(self, arr):         
       
          for i in arr:               
             self.addNewNode(i)

             
     def addNewNode(self, data):
          if self.head == None:
               self.head = Node(data)
          else:
               self.head.appendToTail(data)

     def deleteNode(self,withData):
          n = self.head
          if n.data == withData:
               self.head = n.next
               return self.head
          while n.next != None:
               if n.next.data == withData:
                    n.next = n.next.next
                    return self.head
               n = n.next
          return self.head
     
     def printList(self):
          node = self.head
          while node!= None:   
               print(node.data)
               node = node.next