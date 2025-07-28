"""Q1)Write a program to read the entire content from a txt file and display it to the user."""

filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()  
    print("\n--- File Content ---")
    print(content)

"""Q2)Write a program to read first lines from a txt file. Get n as user input."""

filename = input("Enter the filename: ")
n = int(input("Enter the number of lines to read: "))

with open(filename, 'r') as file:
    print(f"\n--- First {n} lines ---")
    for i in range(n):
        line = file.readline()
        if not line:
            break  
        print(line.strip())  

"""Q3)Write a program to accept Input from user and append it to a txt file."""

filename = input("Enter the filename: ")
text_to_append = input("Enter the text you want to append: ")

with open(filename, 'a') as file:
    file.write(text_to_append + '\n')

print("Text has been appended to the file successfully.")

"""Q4)Write a program to read contents fron a txt file line by line and store each line into
a list."""

filename = input("Enter the filename: ")

lines_list = []
with open(filename, 'r') as file:
    for line in file:
        lines_list.append(line.strip()) 

print("Lines stored in the list:")
print(lines_list)

"""Q5)Write a program to find the longest word from the txt file contents, assuring that the
file will have only one longest word in it."""

filename = input("Enter the filename: ")

longest_word = ""
with open(filename, 'r') as file:
    for line in file:
        words = line.split()  
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

print("The longest word in the file is:", longest_word)

"""Q6)Write a program to count the frequency of a user entered word in a txt file."""

filename = input("Enter the filename: ")
word_to_search = input("Enter the word to search: ")

count = 0
with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word.strip('.,!?').lower() == word_to_search.lower():
                count += 1

print(f"The word '{word_to_search}' appears {count} time(s) in the file.")
