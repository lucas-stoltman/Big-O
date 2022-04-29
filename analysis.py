# Created by Lucas Stoltman
# Program 3
# April 21st, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import bigo
import time
import random

i = 1
min_val = 1
max_val = 1

while i <= 7:
    target = random.randint(min_val, max_val)

    list1 = list(range(min_val, max_val + 1))

    # sort the list for find4() only
    list1.sort()

    total_time = 0
    average_time = 0
    iterations = 10
    for j in range(iterations+1):
        tic = time.perf_counter_ns()
        bigo.find4(list1, target)
        toc = time.perf_counter_ns()
        # print(max_val, "\t{:,}".format(toc - tic))
        # print(max_val)

        # skip the first iteration because it skews the data
        if j >= 1:
            duration = (toc - tic)
            # print(duration)
            total_time += duration
            average_time = total_time // iterations
    print(f"{average_time}")
    max_val *= 10
    i += 1

