"""
Python 3.7
You are given a string 'S' and width 'w'.
Your task is to wrap the string into a paragraph of width 'w'.

Input Format

The first line contains a string, 'S'.
The second line contains the width, 'w'.

Output Format

Print the text wrapped paragraph.
"""

import textwrap


def wrap(string, max_width):
    """Reading and splitting string to substring. Output a result to column."""

    text = textwrap.wrap(string, width=max_width)
    return '\n'.join(text)


if __name__ == '__main__':
    string_1, max_width_1 = input('Please, input a string: '), \
                        int(input('Input a value of max width, which split a string to substring: '))
    result = wrap(string_1, max_width_1)
    print(result)
