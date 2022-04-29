# Created by Lucas Stoltman
# Program 3
# April 16th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import bigo
import timeit
import random

print("---------------------------")
print("Beginning Testing")
print("---------------------------")

min_val = 1
max_val = 10000

# list must be sorted before using either of these values
lower_bound = min_val
upper_bound = max_val+1

target = random.randint(min_val, max_val*2)

print("Initializing list...")
list1 = list(range(min_val, max_val+1))
random.shuffle(list1)

print(f"[{min_val} ... {max_val}]")
print(f"target: {target}")


# --- find1() ---
print("\n---\033[1m", "find1", "\033[0m---", )
t = timeit.Timer(f"find1({list1}, {target})", "from bigo import find1")
duration = t.timeit(1000)
# target : boolean result
print(f"{target} : {bigo.find1(list1, target)}")
print("Time:", duration, "ms")

# --- find2() ---
print("\n---\033[1m", "find2", "\033[0m---", )
t = timeit.Timer(f"find2({list1}, {target})", "from bigo import find2")
duration = t.timeit(1000)
# target : boolean result
print(f"{target} : {bigo.find2(list1, target)}")
print("Time:", duration, "ms")

# # --- find3() ---
print("\n---\033[1m", "find3", "\033[0m---", )
t = timeit.Timer(f"find3({list1}, {target})", "from bigo import find3")
duration = t.timeit(1000)
# target : boolean result
print(f"{target} : {bigo.find3(list1, target)}")
print("Time:", duration, "ms")

# sort the list for find4()
list1.sort()

# --- find4() ---
print("\n---\033[1m", "find4", "\033[0m---", )
t = timeit.Timer(f"find4({list1}, {target})", "from bigo import find4")
duration = t.timeit(1000)
# target : boolean result
print(f"{target} : {bigo.find4(list1, target)}")
print("Time:", duration, "ms")
