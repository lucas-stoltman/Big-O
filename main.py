# Created by Lucas Stoltman
# Program 3
# April 16th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

from bigo import BigO

list1 = [5, 2, 5, 6, 7, 5, 2]

test1 = BigO()

val1 = 7
val2 = 3

print("\n---", "find1", "---", )
print(f"{val1} : " + str(test1.find1(list1, val1)))
print(f"{val2} : " + str(test1.find1(list1, val2)))

# # TODO
# print("\n---", "find2", "---", )
# print(f"{val1} : " + str(test1.find2(list1, val1)))
# print(f"{val2} : " + str(test1.find2(list1, val2)))

print("\n---", "find3", "---", )
print(f"{val1} : " + str(test1.find3(list1, val1)))
print(f"{val2} : " + str(test1.find3(list1, val2)))

# TODO
# print("\n---", "find4", "---", )
# print(f"{val1} : " + str(test1.find4(list1, val1)))
# print(f"{val2} : " + str(test1.find4(list1, val2)))
