"""
Python 3.7.
Given the names and grades for each student in a Physics class of 'N' students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.
Note: If there are multiple students with the same grade, order their names
alphabetically and print each name on a new line.
"""


def print_nested_list():
    students_scores = []
    for _ in range(0, int(input('Input count of students: '))):

        students_scores.append(
            [input('Input name of the {} student: '.format(_)),
             float(input('Input grade of the {} student: '.format(_)))]
        )

    second_lowest = sorted(list(set([scores for name, scores in students_scores])))[1]
    print('\n'.join([name for name, score in sorted(students_scores) if score == second_lowest]))


if __name__ == '__main__':
    print_nested_list()
