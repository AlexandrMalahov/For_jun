"""
Python 3.7
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

Input Format

The first line of input contains the original string.
The next line contains the substring.

Output Format

Output the integer number indicating the total number
of occurrences of the substring in the original string.
"""


def count_substring(string, sub_string):
    """This function returns substring count in string"""

    count = 0
    string = list(string)
    sub_string = list(sub_string)
    for i in range(len(string)):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    STRING_1 = input('Input a string: ').strip()
    SUB_STRING_1 = input('Input a substring: ').strip()
    COUNT_1 = count_substring(STRING_1, SUB_STRING_1)
    print(COUNT_1)
