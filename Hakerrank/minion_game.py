"""
Python 3.7
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, 'S'.
Both players have to make substrings using the letters of the string 'S'.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string 'S'.

For Example:
String 'S' = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""


def minion_game(string):
    """
    Function calculates how many words
    player can create using given string.
    """

    vowels = 'AEIOU'
    kevin_scores = 0
    stuart_scores = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_scores += len(string) - i
        else:
            stuart_scores += len(string) - i
    if kevin_scores > stuart_scores:
        print('Kevin', kevin_scores)
    elif kevin_scores < stuart_scores:
        print('Stuart', stuart_scores)
    else:
        print('Draw')


if __name__ == '__main__':
    string_1 = input('Input a word: ')
    minion_game(string_1)
