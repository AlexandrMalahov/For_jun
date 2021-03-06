"""
Python 3.7
You are given a string 'S'.
Your task is to find out if the string 'S' contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string 'S'.

Constraints


Output Format

In the first line, print True if 'S' has any alphanumeric characters. Otherwise, print False.
In the second line, print True if 'S' has any alphabetical characters. Otherwise, print False.
In the third line, print True if 'S' has any digits. Otherwise, print False.
In the fourth line, print True if 'S' has any lowercase characters. Otherwise, print False.
In the fifth line, print True if 'S' has any uppercase characters. Otherwise, print False."""

if __name__ == '__main__':
    string = input('Please, input a string: ')
    print(any(alpha.isalnum() for alpha in string))
    print(any(alpha.isalpha() for alpha in string))
    print(any(alpha.isdigit() for alpha in string))
    print(any(alpha.islower() for alpha in string))
    print(any(alpha.isupper() for alpha in string))
