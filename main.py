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
max_val = 1000

# list must be sorted before using either of these values
lower_bound = min_val
upper_bound = max_val+1

target = lower_bound
test1 = BigO()

print("Initializing list...")
tic = time.perf_counter_ns()
list1 = list(range(min_val, max_val+1))
random.shuffle(list1)
toc = time.perf_counter_ns()


print(f"list1: {list1}")
print("\nList built in {:,}".format(toc - tic), "nanoseconds")


print("\n---\033[1m", "find1", "\033[0m---", )
tic = time.perf_counter_ns()
print(f"{target} : " + str(test1.find1(list1, target)))
toc = time.perf_counter_ns()
print("{:,}".format(toc - tic), "nanoseconds")

print("\n---\033[1m", "find2", "\033[0m---", )
tic = time.perf_counter_ns()
print(f"{target} : " + str(test1.find2(list1, target)))
toc = time.perf_counter_ns()
print("{:,}".format(toc - tic), "nanoseconds")

print("\n---\033[1m", "find3", "\033[0m---", )
tic = time.perf_counter_ns()
print(f"{target} : " + str(test1.find3(list1, target)))
toc = time.perf_counter_ns()
print("{:,}".format(toc - tic), "nanoseconds")


# sort the list for find4()
list1.sort()

print("\n---\033[1m", "find4", "\033[0m---", )
tic = time.perf_counter_ns()
print(f"{target} : " + str(test1.find4(list1, target)))
toc = time.perf_counter_ns()
print("{:,}".format(toc - tic), "nanoseconds")
