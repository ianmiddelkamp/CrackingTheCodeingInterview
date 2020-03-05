#!/usr/bin/python
# -*- coding: utf-8 -*-
QUESTION = "1.4"

import time


def solve_it(str):
     chars = {}
     lowercase = str.lower()
     for char in lowercase:
          if char.isalpha() == False:
               continue
          elif char in chars:
               count = chars[char]
               count += 1
               chars[char] = count
          else:
               chars[char] = 1
     numwith1count = 0
     for chars,counts in chars.items():
         # print(counts)
          if counts == 1:
               numwith1count +=1 
               if numwith1count > 1:
                    return False
     
     return True


import sys

if __name__ == '__main__':
     start = time.perf_counter()
     isPermOfPalindrome = solve_it("tact coa")
     print(isPermOfPalindrome)
     end = time.perf_counter()

     print('Total Time:\n' + str(end - start))
