"""
Python 3.7
Consider the following:

A string, 'S', of length 'n' where s=C0C1...Cn-1.
An integer, 'k', where 'k' is a factor of 'n'.
We can split 's' into 'n/k' subsegments where each subsegment, 'Ti', consists of a contiguous block of 'k'
characters in 's'. Then, use each 'Ti' to create string 'Ui' such that:

The characters in 'Ui' are a subsequence of the characters in 'Ti'.
Any repeat occurrence of a character is removed from the string such that each character in 'Ui' occurs exactly once.
In other words, if the character at some index 'j' in 'Ti' occurs at a previous index '<j' in 'Ti',
then do not include the character in string 'Ui'.
Given 'S' and 'k', print  lines where each line  denotes string .

Input Format

The first line contains a single string denoting 'S".
The second line contains an integer, 'k', denoting the length of each subsegment.

Output Format

Print 'n/k' lines where each line 'i' contains string 'Ui'.
"""

import textwrap


def merge_the_tools(string, k):
    """
    Split string on substrings, delete repeated letters and output result
    """

    text = textwrap.wrap(string, k)
    list_of_text = []
    for i in range(len(text)):
        list_of_text.append([])
        for j in range(len(text[i])):
            if text[i][j] not in list_of_text[i]:
                list_of_text[i].append(text[i][j])
    for pairs in list_of_text:
        print(''.join(pairs))


if __name__ == '__main__':
    string, value_for_split_to_substring = input('Input a string: '), int(input('Input "int" value for split string to substring: '))
    merge_the_tools(string, value_for_split_to_substring)
