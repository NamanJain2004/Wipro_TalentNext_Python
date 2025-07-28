"""PROJECT1:- Your friend has sent you a text file containing n lines. He sent a secret
message with it, which tells you the place and time where you have to go and meet him.

He challenges you to find it out without seeing the content of the file. He has given
hints to find it. Let's surprise him by breaking the challenge with our python code.

Hints to find the secret message:
1. The number of lines in the file tells you the meeting time.
Note: 1<= number of lines <= 24
If the number of lines is exceeding 12, you need to convert it to 12 hour format.
For example,
         #If the number of lines is 15, then the meeting time is 3 PM.
         #If the number of lines is 10, then the meeting time is 10 AM.

2. The word appearing for the maximum number of times tells you the meeting place.
Note: Meeting place will be a street name.
For example,
        #If the word Oxford appears for the maximum number of times, then meeting place is
         Oxford Street.
        #If the word Park appears for the maximum number of times, then meeting place is Park
         Street.

Sample input 1:  Sample.txt1

Sample output 1:
Meeting time: 9 AM
Meeting place: Park Street
Explanation: Number of lines is 9. The word park appears for the maximum of 15 times

Sample input 2:  Sample.txt2

Sample output 2:
Meeting time: 8 PM
Meeting place: Apollo Street
Explanation: Number of lines is 20 and converting it to 12 hour format we get 8 PM. The word
Apollo appears for the maximum of 25 times."""

from collections import Counter
import re

def get_meeting_time(line_count):
    if line_count <= 12:
        return f"{line_count} AM"
    else:
        return f"{line_count - 12} PM"

def get_meeting_place(text):
    words = re.findall(r'\b\w+\b', text.lower()) 
    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]
    return most_common_word.capitalize() + " Street"

filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        text = file.read()

    line_count = len(lines)
    meeting_time = get_meeting_time(line_count)

    with open(filename, 'r') as file:
        text = file.read()

    meeting_place = get_meeting_place(text)

    print("Meeting time:", meeting_time)
    print("Meeting place:", meeting_place)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
