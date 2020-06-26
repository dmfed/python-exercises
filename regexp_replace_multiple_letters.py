'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:

attraction
buzzzz
Sample Output:

atraction
buz
'''

import re

lines = ['attraction',
         'buzzzz']

for line in lines:
    line = re.sub(r"(\w)\1+", r"\1", line)
    print(line)
