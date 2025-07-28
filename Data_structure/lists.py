"""Q1)Write a program to create a list of 5 integers and display the list items.Access 
Individual elements through index."""

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Fourth element:", numbers[3])
print("Fifth element:", numbers[4])

"""Q2)Write a program to append a new item to the end of the list."""

numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print("Updated list after appending 60:", numbers)

"""Q3)Write program to reverse the order of the items in the list."""

numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print("Reversed list:", numbers)

"""Q4)Write a program to print the number of occurrences of a specified element in a list."""

numbers = [10, 20, 30, 10, 40, 10, 50]
print("List:", numbers)
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print(f"The element {element} appears {count} time(s) in the list.")

"""Q5)Write a program to append the items of list1 to list2 in the front."""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Updated list:", combined_list)

"""Q6)Write a program to insert a new item before the second element in an existing list."""

numbers = [10, 20, 30, 40, 50]
numbers.insert(1, 15)
print("List after inserting 15:", numbers)

"""Q7)write a program to remove the item from a specified index in a list."""

numbers = [10, 20, 30, 40, 50]

index = int(input("Enter the index: "))
if 0 <= index < len(numbers):
    removed_item = numbers.pop(index)
    print(f"Removed item: {removed_item}")
    print("Updated list:", numbers)
else:
    print("Invalid index!")

"""Q8)Write a program to remove the first occurrence of a specified element from a list."""

numbers = [10, 20, 30, 20, 40, 50]

element = int(input("Enter the element to remove: "))
if element in numbers:
    numbers.remove(element)
    print(f"First occurrence of {element} removed.")
    print("Updated list:", numbers)
else:
    print(f"{element} not found in the list.")
