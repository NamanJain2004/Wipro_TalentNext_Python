"""Q1)Write a program to remove a given item from the set."""

my_set = {10, 20, 30, 40, 50}
item_to_remove = 30
my_set.discard(item_to_remove)
print("Updated set:", my_set)

"""Q2)Write a program to create an intersection of sets."""

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print("Intersection of sets:", set1 & set2)

"""Q3)Write a program to create an union of sets."""

set1 = {10, 20, 30}
set2 = {30, 40, 50} 
print("Union of sets:", set1 | set2)

"""Q4)Write a program to find the maximum and minimum value in a set."""

my_set = {15, 8, 22, 5, 19}
print("Maximum value:", max(my_set))
print("Minimum value:", min(my_set))
