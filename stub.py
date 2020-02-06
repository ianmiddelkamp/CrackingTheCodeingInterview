#!/usr/bin/python
# -*- coding: utf-8 -*-
QUESTION = "1.1"

import time


def solve_it(Question):
     print("Question: " + Question)


import sys

if __name__ == '__main__':
     start = time.perf_counter()
     solve_it(QUESTION)
     end = time.perf_counter()

     print('Total Time:\n' + str(end - start))
