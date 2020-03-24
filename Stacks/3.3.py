#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from Stack import Stack
from Stack import Node
from Stack import EmptyStackException

QUESTION = "3.3"


class SetOfStacks:
     capacity = 0
     currentStack = 0
     currentNode = 0
     Stacks = []
     def __init__(self, cap):
          self.capacity = cap
          firstStack = Stack()
          self.Stacks.append(firstStack)

     def generateFromArray(self, arr):        
           for i in range(len(arr)):
               el = arr[i]
               self.push(el)


     def pop(self):
          if self.Stacks[self.currentStack].isEmpty():
               if self.currentStack == 0:
                   raise Exception("Empty Set of Stacks")
               else:
                   self.currentStack = self.currentStack - 1  
                   self.currentNode = self.capacity - 1

          value = self.Stacks[self.currentStack].pop() 
          self.currentNode = self.currentNode - 1
          return value

     def push(self,data):  
         # print(self.currentStack) 
          if self.currentNode == self.capacity:
               nextStack = Stack()               
               nextStack.push(data)
               self.currentNode = 1
               self.currentStack += 1
               self.Stacks.append(nextStack)
          else:
               self.Stacks[self.currentStack].push(data) 
               self.currentNode = self.currentNode + 1
          

     def peek(self):
          if self.currentStack == 0 and self.Stacks[self.currentStack].isEmpty():
               raise EmptyStackException("Empty Stack")
          else:
               return self.Stacks[self.currentStack].peek()
     
     def printSet(self):
          for i in range(self.currentStack,-1, -1):
               Stack = self.Stacks[i]
              
               print("Printing Stack " + str(i))
               print(Stack.returnAsArray())

     def popAt(self, index):
          if index >= 0 and index < len(self.Stacks):
               result = self.Stacks[index].pop()
             
               arrs = []
               newIndex = index
               while newIndex <  len(self.Stacks):
                  
                    arr = self.Stacks[newIndex].returnAsArray()
                    arrs.append(arr)
                    newIndex +=1
               #print(arrs)
               newIndex = 0
              
               while newIndex < len(arrs):
                    j = index + 1
                    if j < len(arrs):
                         itemToAdd = arrs[j].pop(0)
                       #  print(itemToAdd, arrs[j])
                         arrs[newIndex].append(itemToAdd)
                    stack = Stack()
                    stack.generateFromArray(arrs[newIndex])
                    self.Stacks[index] = stack
                   
                    newIndex += 1
                    index +=1 
               #print (arrs)          
               return result
                  
          else: raise Exception("Bad Index")

import sys

if __name__ == '__main__':

     start = time.perf_counter()
     capacity = 3
     arr = [11,5,6,8,3,5,8,9,10,3, 5, 99]    
     print(arr)
     Set = SetOfStacks(capacity)
     Set.generateFromArray(arr) 
     Set.printSet()
     result = Set.popAt(0)
     print(result)
     Set.printSet()
    # Set.printSet()
   