#!/usr/bin/python
# -*- coding: utf-8 -*-
QUESTION = "1.7"

import time


def solve_it(Matrix, Width):
   
    for layer in range(Width):
     
        if layer < Width/2:            
            start = layer
            end = Width - 1 - layer
            for block in range(start, end):
                offset = block - start
             
                saved = Matrix[start][block]
                print(saved)
                Matrix[start][block] = Matrix[end - offset][start]
                Matrix[end - offset][start] =  Matrix[end][end - offset]
                Matrix[end][end - offset] = Matrix[block][end]
                Matrix[block][end] = saved
               # print(Matrix)
    return Matrix
import sys

if __name__ == '__main__':
    start = time.perf_counter()
    testmatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]    
    result = solve_it(testmatrix, len(testmatrix))
    print(result)
    end = time.perf_counter()


    print('Total Time:\n' + str(end - start))
