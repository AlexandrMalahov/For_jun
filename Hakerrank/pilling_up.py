"""
Python 3.7
There is a horizontal row of 'n' cubes. The length of each cube is given.
You need to create a new vertical pile of cubes.
The new pile should follow these directions: if 'CUBEi' is on top of 'CUBEj' then 'SIDE_LENGHTj >= SIDE_LENGHTi'.

When stacking the cubes, you can only pick up either the leftmost or
the rightmost cube each time. Print "Yes" if it is possible to stack the cubes.
Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer 'T", the number of test cases.
For each test case, there are '2' lines.
The first line of each test case contains 'n', the number of cubes.
The second line contains 'n' space separated integers, denoting the sideLengths of each cube in that order.

Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.
"""

if __name__ == '__main__':
    quantity_of_test_cases = int(input('Input number of test cases: '))
    for _ in range(quantity_of_test_cases):
        quantity_of_cubes = int(input('Input quantity of cubes: '))
        side_lenghts = list(map(int, input('Please, input length of cubes sides: ').split()))
        if max(side_lenghts) in (side_lenghts[0], side_lenghts[-1]):
            print('Yes')
        else:
            print('No')
