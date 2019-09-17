"""
Python 3.7
Processing errors ZeroDivisionError and ValueError.

You are given two values 'a' and 'b'.
Perform integer division and print 'a/b'.

Input Format

The first line contains 'T', the number of test cases.
The next 'T' lines each contain the space separated values of 'a' and 'b'.

Output Format

Print the value of 'a/b'.
In the case of ZeroDivisionError or ValueError, print the error code.
"""

number_of_test_cases = int(input('Input number of test cases: '))

for i in range(number_of_test_cases):
    a, b = input('Please, input values of "a" and "b": ').split()
    try:
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as exc:
        print('Error Code:', exc)
    except ValueError as exception:
        print('Error Code:', exception)



