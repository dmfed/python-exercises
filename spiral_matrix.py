#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        side = int(sys.argv[1])
else:
    side = int(input('Please input number of columns/rows: '))

m = [[0 for column in range(side)] for row in range(side)]  # form the array
num = 1  # set the first number
offset = 0  # we'll need this to fill the matrix properly

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
        
    
    


    
    
