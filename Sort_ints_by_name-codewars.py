'''
Hey You !
Sort these integers for me ...

By name ...

Do it now !

Input
Range is 0-999

There may be duplicates

The array may be empty

Example
Input: 1, 2, 3, 4
Equivalent names: "one", "two", "three", "four"
Sorted by name: "four", "one", "three", "two"
Output: 4, 1, 3, 2
Notes
Don't pack words together:
e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
e.g. "one hundred one", "one hundred two"; is same order as "one hundred and one", "one hundred and two"
e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"
'''

'''
I was really funny when test failed because I misspelled "forty" as "fourty" so
the sort order was different :)
'''

def sort_by_name(arr):
    numbers_by_name = []
    mapping = dict()
    for n in arr:
        name = name_int(n)
        numbers_by_name.append(name)
        mapping[name] = n
    numbers_by_name.sort()
    return [mapping[num] for num in numbers_by_name]

def name_int(n: int) -> str:
    digits = {1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine",
                0: "zero"
                }
    tens = {1: "ten",
                2: "twenty",
                3: "thirty",
                4: "forty",
                5: "fifty",
                6: "sixty",
                7: "seventy",
                8: "eighty",
                9: "ninety"
                }
    elevens = {1: "eleven",
                2: "twelve",
                3: "thirteen",
                4: "fourteen",
                5: "fifteen",
                6: "sixteen",
                7: "seventeen",
                8: "eighteen",
                9: "nineteen"
                }
    name = []
    h, n = divmod(n, 100)
    if h:
        name.append(digits[h] + " hundred")

    t, n = divmod(n, 10)
    if t == 1 and n:
        name.append(elevens[n])
        n = 0
    elif t:
        name.append(tens[t])
    
    if len(name) == 0 or n != 0:
        name.append(digits[n])

    return " ". join(name)

print(name_int(311))

print(sort_by_name([1, 0, 659, 30, 536]))