#!/usr/bin/python
# -*- coding: utf-8 -*-
QUESTION = "2.1"

import time
import SingleLinkedList as LL

def solve_it1(arr):
     sll = LL.SingleLinkedList(arr)     
     sllnew = LL.SingleLinkedList([])
     values = set()
     node = sll.head
     while node!= None:   
          if node.data in values:
               pass
          else:
               values.add(node.data)
               sllnew.addNewNode(node.data)          
          node = node.next
     sllnew.printList()
import sys

if __name__ == '__main__':
     start = time.perf_counter()
     arr = [1,5,6,8,3,5,8,9,10,3, 5, 99]
     
     solve_it1(arr)
     end = time.perf_counter()

     print('Total Time:\n' + str(end - start))
