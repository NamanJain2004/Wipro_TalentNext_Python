#Q1.Write a program to check if a given number is Positive, Negative or Zero.
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

#Q2.Write a program to check if a given number is odd or even
num = int(input("enter a number:"))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Q3.Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
num1 = int(input("Enter the first non-negative number: "))
num2 = int(input("Enter the second non-negative number: "))
if num1 % 10 == num2 % 10:
    print("True")
else:
    print("False")

#Q4.Write a program to print numbers from 1 to 10 in a single row with one tab space
for i in range(1, 11):
    print(i, end='\t')

#Q5.Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23,58):
    if i % 2 == 0:
        print(i)

#Q6.Write a program to check if a given number is prime or not. 
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

#Q7.Write a program to print prime numbers between 10 and 99.
for num in range(10, 100):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

#Q8.Write a program to print the sum of all the digits of a given number.
num = input("Enter a number: ")
sum = 0

for digit in num:
    sum += int(digit)
print("Sum of digits:",sum)

#Q9.Write a program to reverse a given number and print.
num = input("Enter a number: ")
reverse = num[::-1]
print("Reversed number:",reverse)

#Q10.Write a program to find if the given number is palindrom or not.
num = input("Enter a number: ")

if num == num[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

