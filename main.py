# Created by Lucas Stoltman
# Program 3
# April 16th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

from bigo import BigO
import time

print("---------------------------")
print("Beginning Testing")
print("---------------------------")

list1 = [5, 2, 5, 6, 7, 5, 2]
print(f"list1: {list1}")

test1 = BigO()

val1 = 7
val2 = 3

print("\n---", "find1", "---", )
tic = time.perf_counter_ns()
print(f"{val1} : " + str(test1.find1(list1, val1)))
print(f"{val2} : " + str(test1.find1(list1, val2)))
toc = time.perf_counter_ns()
print(f"{toc - tic} nanoseconds")

print("\n---", "find2", "---", )
tic = time.perf_counter_ns()
print(f"{val1} : " + str(test1.find2(list1, val1)))
print(f"{val2} : " + str(test1.find2(list1, val2)))
toc = time.perf_counter_ns()
print(f"{toc - tic} nanoseconds")

print("\n---", "find3", "---", )
tic = time.perf_counter_ns()
print(f"{val1} : " + str(test1.find3(list1, val1)))
print(f"{val2} : " + str(test1.find3(list1, val2)))
toc = time.perf_counter_ns()
print(f"{toc - tic} nanoseconds")

# TODO
# print("\n---", "find4", "---", )
# tic = time.perf_counter_ns()
# print(f"{val1} : " + str(test1.find4(list1, val1)))
# print(f"{val2} : " + str(test1.find4(list1, val2)))
# toc = time.perf_counter_ns()
# print(f"{toc - tic} nanoseconds")
