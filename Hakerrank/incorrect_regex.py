"""
Python 3.7
You are given a string 'S'.
Your task is to find out whether 'S' is a valid regex or not.

Input Format

The first line contains integer 'T', the number of test cases.
The next 'T' lines contains the string 'S'.

Output Format

Print "True" or "False" for each test case without quotes.
"""

import re

quantity_of_test_cases = int(input('Input number of test cases: '))
for _ in range(quantity_of_test_cases):
    regex = input('Please, input regex: ')
    try:
        if bool(re.compile(regex)):
            print('True')
    except re.error:
        print('False')
