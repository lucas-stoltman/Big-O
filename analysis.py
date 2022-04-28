# Created by Lucas Stoltman
# Program 3
# April 21st, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

from bigo import BigO
import time
import random

i = 1
min_val = 1
max_val = 1

while i <= 8:
    target = random.randint(min_val, max_val)
    bigo = BigO()

    list1 = list(range(min_val, max_val + 1))

    # sort the list for find4()
    list1.sort()

    tic = time.perf_counter_ns()
    bigo.find4(list1, target)
    toc = time.perf_counter_ns()
    # print(max_val, "\t{:,}".format(toc - tic))
    # print(max_val)
    print(toc - tic)
    max_val *= 10
    i += 1
