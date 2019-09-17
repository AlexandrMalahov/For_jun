"""
Python 3.7
Perform append, pop, popleft and appendleft methods on an empty deque 'd'.

Input Format

The first line contains an integer 'N', the number of operations.
The next 'N' lines contains the space separated names of methods and their values.

Output Format

Print the space separated elements of deque 'd'.
"""

from collections import deque


if __name__ == '__main__':
    quantity_of_operations = int(input('Input quantity of operations: '))
    deq_list = deque()
    for _ in range(quantity_of_operations):
        function, *value = input('Input name of function and values which needs to process: ').split(' ')
        if function == 'append':
            deq_list.append(value)
        elif function == 'appendleft':
            deq_list.appendleft(value)
        elif function == 'pop':
            deq_list.pop()
        elif function == 'popleft':
            deq_list.popleft()
    for value in deq_list:
        print(' '.join(value), end=' ')
