#!/usr/bin/python
# -*- coding: utf-8 -*-
QUESTION = "1.6"

import time


def solve_it(input):
    output = ""
    count = 1
 
    output = ""
    lastindex = len(input) - 1
    for i in range(len(input)):
        char = input[i]
        if i == lastindex:
             output += char + str(count)     

        else:
            nextchar = input[i+1]
            if char == nextchar:
                count += 1
            else:        
                output += char + str(count)        
                count = 1
               
   
    if len(input) < len(output):
        print(input)
    else:
        print(output)


import sys

if __name__ == '__main__':
     start = time.perf_counter()
     teststr = "aabcccccaaa"
     solve_it(teststr)
     end = time.perf_counter()

     print('Total Time:\n' + str(end - start))
