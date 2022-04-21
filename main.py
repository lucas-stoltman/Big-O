# Created by Lucas Stoltman
# Program 3
# April 16th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

from bigo import BigO
import time
import random

print("---------------------------")
print("Beginning Testing")
print("---------------------------")

min_val = 1
max_val = 100
target = 100
test1 = BigO()

list1 = list(range(min_val, max_val+1))
random.shuffle(list1)
print(f"list1: {list1}")

print("\n---", "find1", "---", )
tic = time.perf_counter_ns()
print(f"{target} : " + str(test1.find1(list1, target)))
toc = time.perf_counter_ns()
print("{:,}".format(toc - tic), "nanoseconds")

print("\n---", "find2", "---", )
tic = time.perf_counter_ns()
print(f"{target} : " + str(test1.find2(list1, target)))
toc = time.perf_counter_ns()
print("{:,}".format(toc - tic), "nanoseconds")

print("\n---", "find3", "---", )
tic = time.perf_counter_ns()
print(f"{target} : " + str(test1.find3(list1, target)))
toc = time.perf_counter_ns()
print("{:,}".format(toc - tic), "nanoseconds")


# sort the list for find4()
list1.sort()

print("\n---", "find4", "---", )
tic = time.perf_counter_ns()
print(f"{target} : " + str(test1.find4(list1, target)))
toc = time.perf_counter_ns()
print("{:,}".format(toc - tic), "nanoseconds")
