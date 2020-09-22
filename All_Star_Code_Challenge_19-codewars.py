'''
All Star Code Challenge #19

You work for an ad agency and your boss, Bob, loves a catchy slogan. 
He's always jumbling together "buzz" words until he gets one he likes. 
You're looking to impress Boss Bob with a function that can do his job 
for him.

Create a function called sloganMaker() that accepts an array of string 
"buzz" words. The function returns an array of all possible UNIQUE 
string permutations of the buzz words (concatonated and separated by 
spaces).

Your boss is not very bright, so anticipate him using the same "buzz" 
word more than once, by accident. The function should ignore these 
duplicate string inputs.

sloganMaker(["super", "hot", "guacamole"]);
//[ 'super hot guacamole',
//  'super guacamole hot',
//  'hot super guacamole',
//  'hot guacamole super',
//  'guacamole super hot',
//  'guacamole hot super' ]

sloganMaker(["cool", "pizza", "cool"]); // => [ 'cool pizza', 'pizza cool' ]
Note:
There should be NO duplicate strings in the output array

The input array MAY contain duplicate strings, which should STILL result 
in an output array with all unique strings

An empty string is valid input

The order of the output array must match those rules:

Generate the permutations in lexicographic order of the original array.
keep only the first occurence of a permutation, when duplicates are found.
'''

'''
# This is the PROPER way to get permutations.
from itertools import permutations

def slogan_maker(array):
    answer = []
    nodupes = remove_duplicates(array)
    for perm in permutations(nodupes):
        answer.append(" ".join(perm))
    return answer
'''
def slogan_maker(array):
    s = remove_duplicates(array)
    out = find_permutations(s)
    return out
    
    
def find_permutations(elements):
    '''
    Wrote this one to demo the concept. However the standard library 
    has itertools.permutation, which does lazy calculation with yield
    I'g use that one instead (see commented out cetion in the beginning of solution)
    I've checked and it passes the tests fine.
    '''
    if len(elements) == 1:
        return elements
    result = []
    for i in range(len(elements)):
        remaining = find_permutations(elements[:i] + elements[i+1:])
        for item in remaining:
            result.append(elements[i] + " " + item)
    return result

def remove_duplicates(arr):
    out = []
    for val in arr:
        if val not in out:
            out.append(val)
    return out
