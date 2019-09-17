"""
Python 3.7
A newly opened multinational brand has decided to base their company logo
on the three most common characters in the company name.
They are now trying out various combinations of company names and logos
based on this condition. Given a string 's', which is the company name in
lowercase letters, your task is to find the top three most common characters
in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,
'GOOGLE' would have it's logo with the letters 'G, O, E'.

Input Format

A single line of input containing the string 'S'.

Output Format

Print the three most common characters along with their
occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""

import collections


if __name__ == '__main__':
    company_logo = collections.Counter(input('Input company logo: ').lower())
    logo_counter = collections.Counter.most_common(company_logo)
    for i in range(len(logo_counter)):
        for j in range(len(logo_counter)):
            if logo_counter[i][1] == logo_counter[j][1] and ord(logo_counter[i][0]) < ord(logo_counter[j][0]):
                logo_counter[i], logo_counter[j] = logo_counter[j], logo_counter[i]
    for tup in logo_counter[:3]:
        print(tup[0], tup[1])
