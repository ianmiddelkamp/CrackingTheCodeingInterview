#!/usr/bin/python
# -*- coding: utf-8 -*-
QUESTION = "3.2"

import time
from Stack import Stack
from Stack import Node


class StackWithMin(Stack):
     minstack = None
     def __init__(self):
          super().__init__()
          self.minstack = Stack()


     def pop(self):
          data =  super().pop()
          if data == self.minstack.peek():
              _ = self.minstack.pop()
          return data


     def push(self,data):   
          if self.minstack.isEmpty():
               self.minstack.push(data)
          elif self.minstack.peek() > data:
               self.minstack.push(data)
          super().push(data)

     def getMin(self):
          return self.minstack.peek()

     
     def getMinStack(self):
          return self.minstack


import sys

if __name__ == '__main__':

     start = time.perf_counter()
     arr = [11,5,6,8,3,5,8,9,10,3, 5, 99]     
     stack = StackWithMin()
     stack.generateFromArray(arr)
     print(stack.returnAsArray())  
     print(stack.getMinStack().returnAsArray())
     print(stack.getMinStack().pop())
     print(stack.getMinStack().returnAsArray())
    # print(solve_it1(arr,3))
     end = time.perf_counter()
     print('Total Time:\n' + str(end - start)) 

   
