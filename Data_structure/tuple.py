"""Q1)Write a program to print the 4th element from first and 4th element
from last in a tuple."""

t = (5, 10, 15, 20, 25, 30, 35, 40)
print("4th element from start:", t[3])
print("4th element from end:", t[-4])

"""Q2)Write a program to check whether an element exists in a tuple or not."""

my_tuple = (10, 20, 30, 40, 50)

element = 30
if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

"""Q3)Write a program to convert a list into a tuple."""

my_list = [10, 20, 30, 40, 50]

my_tuple = tuple(my_list)
print("List:", my_list)
print("Tuple:", my_tuple)

"""Q4)Write a program to find the index of an item in a tuple."""

my_tuple = (5, 10, 15, 20, 25)

item = 15
if item in my_tuple:
    index = my_tuple.index(item)
    print(f"Index of {item} is {index}.")
else:
    print(f"{item} is not in the tuple.")

"""Q5)Write a program to replace last value of tuples in a list to 100.
Sample list: [(10,20,40), (40,50,60), (70,80,90)]
Expected Output: [(10,20,100), (40,50,100), (70,80,100)]"""

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

updated_list = [(a, b, 100) for (a, b, c) in sample_list]
print("Updated List:", updated_list)
