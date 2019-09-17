"""
Python 2.7, Wordcount exercise
Google's Python class. Need to find words count
and top of 20 words in file.
"""

import sys


def words_count(filename):
    """
    Helper utility function that reads a file
    and builds and returns a word/count dict for it.
    """

    string_count = {}
    with open(filename, 'r') as f_n:
        string_input = sorted(f_n.read().lower().split())
    for word in string_input:
        count = 0
        for string in string_input:
            if word == string:
                count += 1
        string_count[word] = count
    return string_count


print 'All words'
print


def print_words(filename):
    """
    This function prints words and words count
    with help function 'words_count' as a string.
    """

    words = sorted(words_count(filename).keys())
    for word in words:
        print word + ' ' + str(words_count(filename)[word])


print_words('english_text.txt')

print
print 'Top words'
print


def print_top(filename):
    """
    This function prints top of 20 words which meets in file.
    """

    top_val = sorted(words_count(filename).items(), key=lambda item: item[-1], reverse=True)
    for top in top_val[:20]:
        print top[0] + ' ' + str(top[1])


print_top('english_text.txt')


def main():
    """'
    main()' function calls functions 'print_words' and 'print_top
    '"""

    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
