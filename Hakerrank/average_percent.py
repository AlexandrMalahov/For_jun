"""
Python 3.7
You have a record of 'N' students. Each record contains the student's name, and their percent marks in Maths,
Physics and Chemistry. The marks can be floating values. The user enters some integer 'N' followed by the
names and marks for 'N' students. You are required to save the record in a dictionary data type.
The user then enters a student's name.
Output the average percentage marks obtained by that student, correct to two decimal places.
"""

if __name__ == '__main__':
    quantity_of_students = int(input('Input quantity of students: '))
    student_marks = {}
    for _ in range(quantity_of_students):
        name, *grade = input('Input name and grades of student: ').split()
        scores = list(map(float, grade))
        student_marks[name] = scores
    query_name = input('Input name of student for find his average percent: ')
    average_per = sum(student_marks[query_name]) / len(scores)
    print('{:.2f}'.format(average_per))
