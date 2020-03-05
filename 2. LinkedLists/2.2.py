#!/usr/bin/python
# -*- coding: utf-8 -*-
QUESTION = "2.1"

import time
import SingleLinkedList as LL

def solve_it1(arr, k):
     sll = LL.SingleLinkedList(arr)
     node = sll.head
     node2 = node
     counter = 0
   
     while node!= None:                   
          node = node.next
          if counter < k:
               counter += 1 
          else:
               node2 = node2.next 
     return node2.data




def recurse(ipt, k, index):
     #stop building stack
     if ipt == None:
          return None
     else:    
          #add to stack            
          otp = recurse(ipt.next, k, index)  
          index.value +=1
          if index.value == k:               
               return ipt
          else:
               return otp
               

def solve_it2(arr,k):
     sll = LL.SingleLinkedList(arr)
     node = sll.head
     I = LL.Index()
     node = recurse(node,k, I)
     return node.data
import sys

if __name__ == '__main__':

     start = time.perf_counter()
     arr = [1,5,6,8,3,5,8,9,10,3, 5, 99]     
     print(solve_it1(arr,3))
     end = time.perf_counter()
     print('Total Time:\n' + str(end - start)) 

     start = time.perf_counter()
     arr = [1,5,6,8,3,5,8,9,10,3, 5, 99]
     print(solve_it2(arr,3))
     end = time.perf_counter()
     print('Total Time:\n' + str(end - start)) 
