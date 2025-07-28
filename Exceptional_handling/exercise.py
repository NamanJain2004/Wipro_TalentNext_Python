"""Q1)Write a program to accept the numbers from the user and perform division. If any exception
 occurs, print an error message or else print the result."""

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result of division is:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integer numbers.")
except Exception as e:
    print("An unexpected error occurred:", e)

"""Q2)Write a program to accept a number from the user and check whether it's prime or not.
If user enters anything other than number, handle the exception and print an error message."""

try:
    num = int(input("Enter a number: "))

    if num < 2:
        print(num, "is not a prime number.")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")

except ValueError:
    print("Error: Please enter a valid integer number.")

"""Q3)Write a program to accept the file name to be opened from the user, if file exist print
the contents of the file in title case or else handle the exception and print an error message."""

try:
    filename = input("Enter the file name: ")
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content in title case:\n")
        print(content.title())

except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")
except Exception as e:
    print("An unexpected error occurred:", e)

"""Q4)Declare a list with 10 integers and ask the user to enter an Index. Check whether the
number in that index is positive or negative number. If any invalid index is entered, handle
the exception and print error message."""

numbers = [12, -5, 0, 7, -9, 3, -1, 4, 6, -2]

try:
    index = int(input("Enter an index (0 to 9): "))
    
    num = numbers[index]
    
    if num > 0:
        print(f"The number at index {index} is positive.")
    elif num < 0:
        print(f"The number at index {index} is negative.")
    else:
        print(f"The number at index {index} is zero.")

except IndexError:
    print("Error: Invalid index! Please enter a number between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")
