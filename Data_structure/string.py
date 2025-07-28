"""Q1)Write a program to count the number of upper and lower case letters in a string."""

def count_upper_lower(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_upper_lower("Hello World")

"""Q2)Write a program that will check whether a given string is palindrome or not."""

def is_palindrome(s):
    if s == s[::-1]:
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")

is_palindrome("madam")
is_palindrome("hello")

"""Q3)Given a string, return a new string made of n copies of the first 2 chars of the
original string where n is the length of the string. The string length will be >= 2.
If input is "Wipro" then output should be "WiWiWiWiWi". """

def repeat_front_chars(s):
    front = s[:2]  
    return front * len(s)
print(repeat_front_chars("Wipro"))  

"""Q4)Given a string, if the first or last character is 'x',return the string without
those 'x' character, else return the string unchanged. If the input is "xHix", then 
output is "Hi". """

def remove_x(s):
    if s.startswith('x'):
        s = s[1:]  
    if s.endswith('x'):
        s = s[:-1]  
    return s
print(remove_x("xHix"))   

"""Q5)Given a string and an integer n, return a string made of n repetitions of the last n
characters of the string. You may assume that n is between 0 and the length of the string 
inclusive. For example-if the inputs are "Wipro" and 3, then the output should be "propropro"."""

def repeat_last_n_chars(s, n):
    return s[-n:] * n

input_string = "Wipro"
n = 3
result = repeat_last_n_chars(input_string, n)
print(result)  
