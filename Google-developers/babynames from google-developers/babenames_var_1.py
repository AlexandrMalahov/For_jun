"""
Python 3.7. Функция считывающая данные из html файла.
Нужно считать данные из html таблицы
(имена детей и индекс популярности в определённый год)
и вывести обработанные данные на экран.
"""

import re
from lxml import html


def extract_names(filename):
    """
    Открытие файла, считывание года,
    имён и индекса популярности.
    Использованы регулярные выражения и фунция xpath библиотеки lxml.
    Вывод отсортированного по алфавиту результата на экран.
    """

    with open(filename, 'r') as f:
        tree = html.fromstring(f.read())
    with open(filename, 'r') as fn:                  # Этот способ позволяет
        year = re.findall(r'Popularity\s'            # вытаскивать год из любого данного файла,
                          r'in\s(\d{4})', fn.read()) # но приходится открывать файл 2 раза.
    print(year[0])
    baby_list = []
    for rating in tree.xpath('body/table/tr/td/table/tr[@align="right"]'):
        baby_list.append(rating[1].text + ' ' + rating[0].text)
        baby_list.append(rating[2].text + ' ' + rating[0].text)
    for baby in sorted(baby_list):
        print(baby)


extract_names('baby2008.html')