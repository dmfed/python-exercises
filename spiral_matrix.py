#!/usr/bin/env python3
'''
This funny piece of code forms a square with side equal to input int
and fills it with numbers from 1 to (side ** 2) in form
of a spiral.
'''
side = int(input('Please input number of columns/rows: '))

m = [[0 for column in range(side)] for row in range(side)]  
num = 1
offset = 0

while side >= 1:
    for i in range(side):  # this fills upper quarter and center of the array
        m[offset][offset + i] = num
        num += 1
    for i in range(side - 1):  # this fills right quarted of the array
        m[i + offset +1][side - 1 + offset] = num
        num += 1
    for i in range(side - 1):  # lower quarter
        m[side + offset - 1][- offset - 2 - i] = num
        num += 1
    for i in range(side - 2):  # left quarter
        m[- offset - 2 - i][offset] = num
        num += 1
    offset += 1
    side -= 2

for y in range(len(m)):  #let's print out the result
    for x in range(len(m[0])):
        print(m[y][x], end = '\t')
    print('\n')
