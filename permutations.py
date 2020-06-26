'''
Find all permutations of an input string.
'''
def find_permutations(elements):
    if len(elements) == 1:
        return elements
    result = []
    for i in range(len(elements)):
        remaining = find_permutations(elements[:i] + elements[i+1:])
        for item in remaining:
            result.append(elements[i] + item)
    return result

result = find_permutations("abcd")
for i in result:
    print(i)
